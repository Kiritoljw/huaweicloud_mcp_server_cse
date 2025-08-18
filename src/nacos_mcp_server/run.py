from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.server import Settings
import logging
from nacos_tools import create_nacos_client

# 日志配置
logger = logging.getLogger()
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('mcp-server-cse-python.log', mode='a')
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Initialize FastMCP server
mcp = FastMCP("Nacos-mcp-server")
settings = Settings()

settings.debug = True
settings.host = "127.0.0.1"
settings.host = 8000


# 配置信息
TOKEN = "your_token_here"  # 从环境变量或配置文件读取
PROJECT_ID = "79c4086f5f3a4e34a92601dfc64b1e8c" # API Explorer查询
NACOS_URL = "http://100.85.123.17:8848/nacos/v1" 

# 创建 Nacos 客户端
nacos_client = create_nacos_client(NACOS_URL, TOKEN, PROJECT_ID)

# ==================== MCP工具函数 ====================

@mcp.tool()
def NacosRegisterInstance(ip: str, port: int, serviceName: str, namespaceId: str = "public", 
                         ephemeral: bool = False, enabled: bool = True, healthy: bool = True):
    """注册实例到服务"""
    return nacos_client.register_instance(ip, port, serviceName, namespaceId, ephemeral, enabled, healthy)

@mcp.tool()
def NacosDeregisterInstance(ip: str, port: int, serviceName: str, namespaceId: str = "public", 
                           ephemeral: bool = False):
    """从服务中删除实例"""
    return nacos_client.deregister_instance(ip, port, serviceName, namespaceId, ephemeral)

@mcp.tool()
def NacosModifyInstance(ip: str, port: int, serviceName: str, namespaceId: str = "public", 
                       ephemeral: bool = False, enabled: bool = True):
    """修改实例信息"""
    return nacos_client.modify_instance(ip, port, serviceName, namespaceId, ephemeral, enabled)

@mcp.tool()
def NacosQueryInstances(serviceName: str, namespaceId: str = "public", healthyOnly: bool = False):
    """查询服务的实例列表"""
    return nacos_client.query_instances(serviceName, namespaceId, healthyOnly)

@mcp.tool()
def NacosQueryInstanceDetail(ip: str, port: int, serviceName: str, namespaceId: str = "public", 
                            ephemeral: bool = False):
    """查询实例详细信息"""
    return nacos_client.query_instance_detail(ip, port, serviceName, namespaceId, ephemeral)

@mcp.tool()
def NacosSendInstanceBeat(ip: str, port: int, serviceName: str, namespaceId: str = "public"):
    """发送实例心跳"""
    return nacos_client.send_instance_beat(ip, port, serviceName, namespaceId)

@mcp.tool()
def NacosCreateService(serviceName: str, namespaceId: str = "public"):
    """创建服务"""
    return nacos_client.create_service(serviceName, namespaceId)

@mcp.tool()
def NacosDeleteService(serviceName: str, namespaceId: str = "public"):
    """删除服务"""
    return nacos_client.delete_service(serviceName, namespaceId)

@mcp.tool()
def NacosUpdateService(serviceName: str, namespaceId: str = "public"):
    """更新服务"""
    return nacos_client.update_service(serviceName, namespaceId)

@mcp.tool()
def NacosQueryService(serviceName: str, namespaceId: str = "public"):
    """查询服务详细信息"""
    return nacos_client.query_service(serviceName, namespaceId)

@mcp.tool()
def NacosQueryServiceList(pageNo: int = 1, pageSize: int = 10, namespaceId: str = "public"):
    """查询服务列表"""
    return nacos_client.query_service_list(pageNo, pageSize, namespaceId)

@mcp.tool()
def QuerySystemSwitches():
    """查询系统开关"""
    return nacos_client.query_system_switches()

@mcp.tool()
def UpdateSystemSwitches(entry: str, value: str, debug: bool = True):
    """更新系统开关"""
    return nacos_client.update_system_switches(entry, value, debug)

@mcp.tool()
def QuerySystemMetrics():
    """查询系统当前数据指标"""
    return nacos_client.query_system_metrics()

@mcp.tool()
def QueryServerList():
    """查询服务器列表"""
    return nacos_client.query_server_list()

@mcp.tool()
def UpdateInstanceHealthStatus(serviceName: str, ip: str, port: int, clusterName: str, 
                              healthy: bool = True, namespaceId: str = "public"):
    """更新实例健康状态"""
    return nacos_client.update_instance_health(serviceName, ip, port, clusterName, healthy, namespaceId)

if __name__ == "__main__":
    mcp.run(transport="sse")