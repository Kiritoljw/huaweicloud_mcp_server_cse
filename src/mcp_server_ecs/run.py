from mcp.server.fastmcp import FastMCP
import os
import logging
import httpx
import requests


#创建日志器
logger = logging.getLogger()
#设置日志级别
logger.setLevel(logging.INFO)

#创建控制台处理器（StreamHandler）
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#创建文件处理器（FileHandler）
file_handler = logging.FileHandler('NovaListServers-server-python.log', mode='a')
file_handler.setLevel(logging.INFO)

#创建日志格式器
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

#将格式器添加到处理器
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

#将处理器添加到日志器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

#Initialize FastMCP server
mcp = FastMCP("ShowServer")

#通过postman请求获得，去华为云官网查看如何获取iam_auth_token
TOKEN = "MIIXCAYJKoZIhvcNAQcCoIIW+TCCFvUCAQExDTALBglghkgBZQMEAgEwghSTBgkqhkiG9w0BBwGgghSEBIIUgHsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjUtMDctMjNUMTE6MTY6MjkuNDIxMDAwWiIsInNpZ25hdHVyZSI6IkVBcGpiaTF1YjNKMGFDMDNBQUFBQUFBQUJFaHc3ZFFuZU1nUktHWTN2aWtSdC9kck50dDBJQ1JUdUpuVW00WTUwSXgxY1Uzc2pvTkdQdFZXYWRUVkpxUjErWS9DK3BuU3JkdEE0Zm12Tk9MbUNhTnNUcWRIcnZXckRMV1hlKytiaCtJd3pZbC9GekMxZVhmL3hVNjNTRTF1enRwT1Npd3FHUFczK0ZEN205Z0VHNW9OOGJ6NGRmSDhoY0VDeklmN0QyNXJwUW8xS1Zrclo5ems3QURudHQ4Sy9HVlhkYVdjaGZFdzdpV0NSdVhYcUJ6K1RsTW9OK1VEZ096WWxTTnVBMjZubzlZYUlLbURCWW5zdlM1dmF0SWNCb2FaejF6TkFjVGtpeU5GS2hRSktTSGpaSGFSK1B6eEk1emRrbXBnQk1lM3BzMnVGd3V0LzJEYlpmZlNId3hSOFJLM3A3TldnbEQ2QUQyN0dWeWhmK1BkIiwibWV0aG9kcyI6WyJwYXNzd29yZCJdLCJjYXRhbG9nIjpbXSwicm9sZXMiOlt7Im5hbWUiOiJ0ZV9hZG1pbiIsImlkIjoiMCJ9LHsibmFtZSI6ImNjaV9hZG0iLCJpZCI6IjAifSx7Im5hbWUiOiJvYnNfYl9saXN0IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGNzX21zX3J3cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfY3NzX3NlcnZlcmxlc3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2VfdHVyYm9fZW5oYW5jZWQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2Nsb3VkZGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2ZhYnJpYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfcm9ja2V0bXFfc2VydmVybGVzcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21lZXRpbmdfZW5kcG9pbnRfYnV5IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfY3IiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX211bHRpX2Nsb3VkX3ZlcnNpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zaXNfc2Fzcl9lbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NmdyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX2lydGMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfY29jX2NhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcmVkaXM2LWdlbmVyaWMtaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaV9rb29waG9uZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX2V2c19lc3NkMiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLWVudGVycHJpc2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jb2NfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pZG1lX21ibV9mb3VuZGF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3ZyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWFzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfa29vcGhvbmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2t2cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX211bHRpX2JpbmQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9yb21hZXhjaGFuZ2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX21nY19iaWdkYXRhbWlncmF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2VyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfa29vbWFwIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX2Vzc2QyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcGVkYV9zY2hfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF91Y3NfY2lhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2llIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaHdkZXYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfY2NlX2F1dG9waWxvdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfZWxhc3RpY19uYXQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kYXl1X2RsbV9jbHVzdGVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2FjNyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2hzZC1wdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NvbXBhc3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ubHBfbGdfdGciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pYW1faWRlbnRpdHljZW50ZXJfY24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfcmdjX2ludGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zZnNfbGlmZWN5Y2xlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW90ZWRnZV9iYXNpYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NlcnZpY2VzdGFnZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FwcHN0YWdlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfb25ldGFsayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3VjcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JpX2R3cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2F0YyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Jjc19uZXNfc2ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zaXNfYXNzZXNzX2F1ZGlvIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3NjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9pX2Nsb3VkcG9uZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Vjc19vbl9wcmVtaXNlc19pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfZGRzX2FybSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2VjcCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaWRlZV9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lkbWVfbGlua3hfZm91bmRhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLXJlZGlzNi1nZW5lcmljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfdGVzdGdvbmdjZTAxMjYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbXMtcm9ja2V0bXE1LWJhc2ljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGx2X29wZW5fYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2ZpbmVfZ3JhaW5lZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2Nlc193YW5tb25pdG9yX2NuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfS29vTWVzc2FnZUNPQlQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbXNfcmVsaWFiaWxpdHkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF90ZXN0Z29uZ2NlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfdGVzdGdvbmdjZTAxMjYyMyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JnYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lkdF9kbWUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9hYzciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9zZnN0dXJib2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9sZWdhY3kiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfd3NhX2NhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZG1zLWFtcXAtYmFzaWMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kZXZjbG91ZF9vdmVyc2VhX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iY2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2VfYXV0b3BpbG90IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW50bF9jb21wYXNzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdWNzX29uX2F3c19pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9kZnBzZXJ2aWNlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfV2VMaW5rX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX3JvdW5kdGFibGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pb3RhbmFseXRpY3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2NyYWZ0YXJ0c3NpbV9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lwc2VjdnBuX09CVCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfZWdfcm91dGVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZHdyX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9JUERDZW50ZXJfQ0FfMjAyMzA4MzAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9tZ2MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF92aXNpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3MzLWVudGVycHJpc2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF91Y3Nfb25wcmVtaXNlcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3dpZmktYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaV9zZnNfbGlmZWN5Y2xlIiwiaWQiOiIwIn0seyJuYW1lIjoiMzIsNDEsMzQwLDIwNyw5LDE2NCwyMjgsNDAiLCJpZCI6IjgifSx7Im5hbWUiOiIyNiIsImlkIjoiOSJ9XSwicHJvamVjdCI6eyJkb21haW4iOnsibmFtZSI6InBhYXNfY3NlX2x3eDQxMDk0MF8wMSIsImlkIjoiZmNhYTRjMGQxOGUyNGRmMzhlODgxYzI4ZWM0ZGRiNWUifSwibmFtZSI6ImNuLW5vcnRoLTciLCJpZCI6Ijc5YzQwODZmNWYzYTRlMzRhOTI2MDFkZmM2NGIxZThjIn0sImlzc3VlZF9hdCI6IjIwMjUtMDctMjJUMTE6MTY6MjkuNDIxMDAwWiIsInVzZXIiOnsiZG9tYWluIjp7Im5hbWUiOiJwYWFzX2NzZV9sd3g0MTA5NDBfMDEiLCJpZCI6ImZjYWE0YzBkMThlMjRkZjM4ZTg4MWMyOGVjNGRkYjVlIn0sIm5hbWUiOiJ3dXpoaWhlbmciLCJwYXNzd29yZF9leHBpcmVzX2F0IjoiMjAyMy0wMy0xOFQwMjozMjoxMy4wMDAwMDBaIiwiaWQiOiIxNjA3NzY1YzAyOGU0OTYzYTUxODI1YTI5MzI3ZmIyMSJ9fX0xggJIMIICRAIBATCBnjCBhTELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCUd1YW5nRG9uZzERMA8GA1UEBwwIU2hlblpoZW4xLjAsBgNVBAoMJUh1YXdlaSBTb2Z0d2FyZSBUZWNobm9sb2dpZXMgQ28uLCBMdGQxDjAMBgNVBAsMBUNsb3VkMQ8wDQYDVQQDDAZpYW1wa2kCFF5Nhgd5lJK8NiTuBYBLAwRkSdmjMAsGCWCGSAFlAwQCATANBgkqhkiG9w0BAQEFAASCAYAHN4LL8sSwWfU5+aCaIa1eEGofFg131EiZIrfcyqMt3UVfUFoaU5C0QhoSHcNWaAGKNcHdFEF3iqYhedsyIW9uqU+sZmKZQwq0n5EwyNaRX33BPiOyn-yjEYMtmYeKgr3auIzivv7z2lR95fMjFgrXMRCF1eCOGjrjYgggVN7Ohj6+gDQ92a97h1jF1M7fJURVAgpJ-U7q+WTWDWK-XNqbQ+KiYcd+F36Ttkehb6nRKWgAh2AqpjMS4t7rIR9fG3xSmk89PGJ25myo0OyZVEoA6jjV6zui-o5QgoyVUk511UKW8qHBGfkZb4WaSaoGZqM3amIdrq9IOfA1FMUOBliS-JvaCuYApclNGL30PZQudTsa7g7pwcVYYvh9CogJhNqvdBZ9k1Fof7y3KJK5oFD6miuVApCKca4MP+uJoJXRbtEqVbHAuTjJcUYjHNvzzQmLXPiijE8Ypkw51GL3monAg7mzPx5Ff+rPt0UPJ2eMlVkVObHKL-tJFEqqGAWASE8="

#在华为云官网中查看
Project_id = "79c4086f5f3a4e34a92601dfc64b1e8c"

@mcp.tool()
def ShowServer(server_id: str) -> dict:
    """
    功能：查询弹性云服务器的详细信息。
    
    Args:
        server_id (str): 云服务器ID
        
    Returns:
        dict: 服务器详细信息或错误信息
    """
    # 参数验证
    if not server_id or not server_id.strip():
        logger.error("server_id参数不能为空")
        return {"error": "server_id参数不能为空"}
    
    # 构建API请求
    base_url = "https://ecs.cn-north-7.ulanqab.huawei.com/v1"  # 乌兰察布
    url = f"{base_url}/{Project_id}/cloudservers/{server_id}"  

    headers = {
        'X-Auth-Token': TOKEN,
        'Content-Type': 'application/json'
    }

    try:
        logger.info(f"正在查询服务器详情，ID: {server_id}")
        response = requests.get(url, headers=headers, verify=False, timeout=30)  # 需要跳过SSL证书验证，因为本地没有证书，添加超时和SSL验证
        response.raise_for_status()
        
        data = response.json()
        server_info = data.get('server', {})  #  修正：直接从data获取server字段
        
        if not server_info:
            logger.warning(f"未找到服务器信息，ID: {server_id}")
            return {"error": f"未找到服务器 {server_id}"}
            
        logger.info(f"成功获取服务器信息，名称: {server_info.get('name', 'Unknown')}")
        return server_info
        
    except requests.exceptions.Timeout:
        logger.error(f"请求超时，服务器ID: {server_id}")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            logger.error(f"服务器不存在，ID: {server_id}")
            return {"error": f"服务器 {server_id} 不存在"}
        else:
            logger.error(f"HTTP错误：{e.response.status_code} - {e}")
            return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def NovaListServers(limit:str):
    """
    调用OpenStack Nova API列出服务器实例。
    
    Args: 
        limit (str): 限制返回的服务器数量，默认10
        
    Returns:
        list: 包含服务器信息的列表，每个服务器包含'name'、'links'以及'id'
    """
    #根据账号下的地址去填写正确的请求头
    base_url = "https://ecs.cn-north-7.ulanqab.huawei.com/v2.1"
    url = f"{base_url}/{Project_id}/servers"
    params = {
        'limit' : limit
    }

    headers = {
        'X-Auth-Token': TOKEN,
        'Content-Type': 'application/json'
    }

    try:
        logger.info(f"正在请求ECS服务器列表,限制数量: {limit}")
        response = requests.get(url, headers=headers, params=params, verify=False)#跳过SSL证书验证（ 生产环境不推荐）
        response.raise_for_status() #检查HTTP响应是否成功，4xx/5xx会抛出异常

        data = response.json()
        servers = data.get('servers', [])
        logger.info(f"成功获取 {len(servers)} 台服务器信息")
        return servers
    except requests.exceptions.RequestException as e:
        print(f"请求失败:{e}")
        return []
    except ValueError as e:
        print(f"无效的JSON响应:{e}")
        return []
    
if __name__ == "__main__":
    mcp.run(transport="sse",port=8001)