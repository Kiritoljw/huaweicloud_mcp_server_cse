import logging
import requests
from typing import Dict, List, Any, Optional, Union


class NacosClient:
    """
    华为云 CSE Nacos 客户端工具类
    提供 Nacos 服务发现和配置管理的所有功能
    """
    
    def __init__(self, base_url: str, token: str, project_id: str = None, timeout: int = 30):
        """
        初始化 Nacos 客户端
        
        Args:
            base_url (str): Nacos 服务器地址，例如 "http://100.85.123.17:8848/nacos/v1"
            token (str): 华为云 IAM 认证令牌
            project_id (str, optional): 华为云项目ID
            timeout (int): 请求超时时间，默认30秒
        """
        self.base_url = base_url.rstrip('/')
        self.token = token
        self.project_id = project_id
        self.timeout = timeout
        self.logger = self._setup_logger()
        
    def _setup_logger(self) -> logging.Logger:
        """设置日志器"""
        logger = logging.getLogger(f"{__name__}.NacosClient")
        if not logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.setLevel(logging.INFO)
        return logger
    
    def _get_headers(self) -> Dict[str, str]:
        """获取请求头"""
        return {
            'X-Auth-Token': self.token,
            'Content-Type': 'application/json'
        }
    
    def _make_request(self, method: str, endpoint: str, params: Dict = None, data: Dict = None) -> Union[Dict, str]:
        """
        统一的HTTP请求方法
        
        Args:
            method (str): HTTP方法 (GET, POST, PUT, DELETE)
            endpoint (str): API端点
            params (dict): URL参数
            data (dict): 请求体数据
            
        Returns:
            Union[Dict, str]: 响应数据或错误信息
        """
        url = f"{self.base_url}{endpoint}"
        headers = self._get_headers()
        
        try:
            self.logger.info(f"发送 {method} 请求到 {endpoint}")
            response = requests.request(
                method=method,
                url=url,
                params=params,
                json=data,
                headers=headers,
                verify=False,
                timeout=self.timeout
            )
            response.raise_for_status()
            
            # 处理不同类型的响应
            response_text = response.text.strip()
            content_type = response.headers.get('content-type', '').lower()
            
            # 特殊处理 Nacos 常见的成功响应
            if response_text == 'ok':
                self.logger.debug(f"收到成功响应: {response_text}")
                return {"success": True, "message": "操作成功"}
            
            if 'application/json' in content_type:
                try:
                    return response.json()
                except ValueError as json_error:
                    # JSON 解析失败，检查是否是简单的文本响应
                    if response_text:
                        self.logger.debug(f"收到非JSON响应: '{response_text}'")
                        # 对于简单的文本响应，返回包装后的结构
                        return {"success": True, "message": response_text}
                    else:
                        self.logger.warning(f"JSON解析失败且响应为空: {json_error}")
                        return {"error": "响应为空"}
            else:
                # 非JSON响应，直接返回文本内容（如果有的话）
                return {"success": True, "message": response_text} if response_text else {"error": "响应为空"}
                
        except requests.exceptions.Timeout:
            error_msg = f"{method} {endpoint} 请求超时"
            self.logger.error(error_msg)
            return {"error": "请求超时"}
        except requests.exceptions.HTTPError as e:
            error_msg = f"HTTP错误: {e.response.status_code} - {e}"
            self.logger.error(error_msg)
            return {"error": f"HTTP错误: {e.response.status_code}"}
        except requests.exceptions.RequestException as e:
            error_msg = f"网络请求失败: {e}"
            self.logger.error(error_msg)
            return {"error": "网络请求失败"}
        except Exception as e:
            error_msg = f"未预期错误: {e}"
            self.logger.error(error_msg)
            return {"error": "服务内部错误"}

    # ==================== 实例管理 ====================
    
    def register_instance(self, ip: str, port: int, service_name: str, 
                         namespace_id: str = "public", ephemeral: bool = False, 
                         enabled: bool = True, healthy: bool = True) -> Union[Dict, str]:
        """注册实例到服务"""
        params = {
            'ip': ip,
            'port': port,
            'serviceName': service_name,
            'namespaceId': namespace_id,
            'ephemeral': ephemeral,
            'enabled': enabled,
            'healthy': healthy
        }
        return self._make_request('POST', '/ns/instance', params=params)
    
    def deregister_instance(self, ip: str, port: int, service_name: str,
                           namespace_id: str = "public", ephemeral: bool = False) -> Union[Dict, str]:
        """从服务中删除实例"""
        params = {
            'ip': ip,
            'port': port,
            'serviceName': service_name,
            'namespaceId': namespace_id,
            'ephemeral': ephemeral
        }
        return self._make_request('DELETE', '/ns/instance', params=params)
    
    def modify_instance(self, ip: str, port: int, service_name: str,
                       namespace_id: str = "public", ephemeral: bool = False,
                       enabled: bool = True) -> Union[Dict, str]:
        """修改实例信息"""
        params = {
            'ip': ip,
            'port': port,
            'serviceName': service_name,
            'namespaceId': namespace_id,
            'ephemeral': ephemeral,
            'enabled': enabled
        }
        return self._make_request('PUT', '/ns/instance', params=params)
    
    def query_instances(self, service_name: str, namespace_id: str = "public",
                       healthy_only: bool = False) -> Dict:
        """查询服务的实例列表"""
        params = {
            'serviceName': service_name,
            'namespaceId': namespace_id,
            'healthyOnly': healthy_only
        }
        return self._make_request('GET', '/ns/instance/list', params=params)
    
    def query_instance_detail(self, ip: str, port: int, service_name: str,
                             namespace_id: str = "public", ephemeral: bool = False) -> Dict:
        """查询实例详细信息"""
        params = {
            'ip': ip,
            'port': port,
            'serviceName': service_name,
            'namespaceId': namespace_id,
            'ephemeral': ephemeral
        }
        return self._make_request('GET', '/ns/instance', params=params)
    
    def send_instance_beat(self, ip: str, port: int, service_name: str,
                          namespace_id: str = "public") -> Union[Dict, str]:
        """发送实例心跳"""
        params = {
            'ip': ip,
            'port': port,
            'serviceName': service_name,
            'namespaceId': namespace_id
        }
        return self._make_request('PUT', '/ns/instance/beat', params=params)
    
    def update_instance_health(self, service_name: str, ip: str, port: int,
                              cluster_name: str, healthy: bool = True,
                              namespace_id: str = "public") -> Union[Dict, str]:
        """更新实例健康状态（仅在集群健康检查关闭时生效）"""
        params = {
            'serviceName': service_name,
            'ip': ip,
            'port': port,
            'clusterName': cluster_name,
            'healthy': healthy,
            'namespaceId': namespace_id
        }
        return self._make_request('PUT', '/ns/health/instance', params=params)

    # ==================== 服务管理 ====================
    
    def create_service(self, service_name: str, namespace_id: str = "public") -> Union[Dict, str]:
        """创建服务"""
        params = {
            'serviceName': service_name,
            'namespaceId': namespace_id
        }
        return self._make_request('POST', '/ns/service', params=params)
    
    def delete_service(self, service_name: str, namespace_id: str = "public") -> Union[Dict, str]:
        """删除服务（仅在实例数为0时允许）"""
        params = {
            'serviceName': service_name,
            'namespaceId': namespace_id
        }
        return self._make_request('DELETE', '/ns/service', params=params)
    
    def update_service(self, service_name: str, namespace_id: str = "public") -> Union[Dict, str]:
        """更新服务"""
        params = {
            'serviceName': service_name,
            'namespaceId': namespace_id
        }
        return self._make_request('PUT', '/ns/service', params=params)
    
    def query_service(self, service_name: str, namespace_id: str = "public") -> Dict:
        """查询服务详细信息"""
        params = {
            'serviceName': service_name,
            'namespaceId': namespace_id
        }
        return self._make_request('GET', '/ns/service', params=params)
    
    def query_service_list(self, page_no: int = 1, page_size: int = 10,
                          namespace_id: str = "public") -> Dict:
        """查询服务列表"""
        params = {
            'pageNo': page_no,
            'pageSize': page_size,
            'namespaceId': namespace_id
        }
        return self._make_request('GET', '/ns/service/list', params=params)

    # ==================== 系统管理 ====================
    
    def query_system_switches(self) -> Dict:
        """查询系统开关"""
        return self._make_request('GET', '/ns/operator/switches')
    
    def update_system_switches(self, entry: str, value: str, debug: bool = True) -> Dict:
        """更新系统开关"""
        params = {
            'entry': entry,
            'value': value,
            'debug': debug
        }
        return self._make_request('PUT', '/ns/operator/switches', params=params)
    
    def query_system_metrics(self) -> Dict:
        """查询系统当前数据指标"""
        return self._make_request('GET', '/ns/operator/metrics')
    
    def query_server_list(self) -> Dict:
        """查询服务器列表"""
        return self._make_request('GET', '/ns/operator/servers')
    
    def query_cluster_leader(self) -> Dict:
        """查询当前集群leader（注意：该API可能已停用）"""
        return self._make_request('GET', '/ns/raft/leader')


# ==================== 便捷函数 ====================

def create_nacos_client(base_url: str, token: str, project_id: str = None) -> NacosClient:
    """
    创建 Nacos 客户端的便捷函数
    
    Args:
        base_url (str): Nacos 服务器地址
        token (str): 华为云 IAM 认证令牌
        project_id (str, optional): 华为云项目ID
        
    Returns:
        NacosClient: Nacos 客户端实例
    """
    return NacosClient(base_url, token, project_id)


# ==================== 使用示例 ====================

if __name__ == "__main__":
    # 使用示例
    
    # 配置参数
    NACOS_URL = "http://100.85.123.17:8848/nacos/v1"
    TOKEN = "your_iam_token_here"
    PROJECT_ID = "your_project_id_here"
    
    # 创建客户端
    client = create_nacos_client(NACOS_URL, TOKEN, PROJECT_ID)
    
    # 示例操作
    try:
        # 创建服务
        result = client.create_service("test-service")
        print("创建服务结果:", result)
        
        # 注册实例
        result = client.register_instance("192.168.1.100", 8080, "test-service")
        print("注册实例结果:", result)
        
        # 查询实例列表
        instances = client.query_instances("test-service")
        print("实例列表:", instances)
        
        # 发送心跳
        result = client.send_instance_beat("192.168.1.100", 8080, "test-service")
        print("心跳结果:", result)
        
    except Exception as e:
        print(f"操作失败: {e}")