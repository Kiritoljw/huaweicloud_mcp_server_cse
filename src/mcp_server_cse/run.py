from mcp.server.fastmcp import FastMCP
import logging
import requests



#创建日志器
logger = logging.getLogger()
#设置日志级别
logger.setLevel(logging.INFO)

#创建控制台处理器（StreamHandler）
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

#创建文件处理器（FileHandler）
file_handler = logging.FileHandler('mcp-server-cse-python.log', mode='a')
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
mcp = FastMCP("CSEEngineServer")

#通过postman请求获得，去华为云官网查看如何获取iam_auth_token
TOKEN = "MIIXQQYJKoZIhvcNAQcCoIIXMjCCFy4CAQExDTALBglghkgBZQMEAgEwghTMBgkqhkiG9w0BBwGgghS9BIIUuXsidG9rZW4iOnsiZXhwaXJlc19hdCI6IjIwMjUtMDctMjlUMDM6Mzg6NDkuMjczMDAwWiIsInNpZ25hdHVyZSI6IkVCQmpiaTF6YjNWMGFIZGxjM1F0TWpVeUFBQUFBQUFBQVJ1aUljb0V0bytnanhRSFJ2RVFPOVJCUjRFOHgwem4zU0VzSWxhZmhQWVU2V0xGdmpXOFVKdEZ4dFQ2OUlYZmd5YVZhdWFNU1BoSlJNOTNCazdwQmFZVXB3STRwTW1yU0ZOQkdnWVpMUmNjeXZvTkFWL3dXbTJXZmcrMjUya1d6MmtORHU5TC81YWU3cFhHVHZYTVE4bEJuYmp2bGFwUWd6dzcrd0ZQU3RFS2NTTTZWSEgrOFc4Wk5KM2R2d2VieVVXU1J1SzN0bGpObjI1RHZ5M3UvZlNQVldNM04rbThpR2IwL1o3OW8yWGNRbE5pdjBNcGppTzVaaXEyNWNNTXpZa25sM1ZEUnU0ODh3TGtwcFR4WVpOOE1FeE5TRGFEM3JhYkU1SHFYTU1FSm1RSmRIZnN0cjFnMVFpMElYcjYvN2U1NEtjdjBKMUZYZi9lMldTSzNFWTIiLCJtZXRob2RzIjpbInBhc3N3b3JkIl0sImNhdGFsb2ciOltdLCJyb2xlcyI6W3sibmFtZSI6InRlX2FkbWluIiwiaWQiOiIwIn0seyJuYW1lIjoiY2NpX2FkbSIsImlkIjoiMCJ9LHsibmFtZSI6Im9ic19iX2xpc3QiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3NfbXNfcndzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9jc3Nfc2VydmVybGVzcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NjZV90dXJib19lbmhhbmNlZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfY2xvdWRkYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfZmFicmljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9yb2NrZXRtcV9zZXJ2ZXJsZXNzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWVldGluZ19lbmRwb2ludF9idXkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9jciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfbXVsdGlfY2xvdWRfdmVyc2lvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Npc19zYXNyX2VuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2Z3IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfaXJ0YyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaV9jb2NfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9yZWRpczYtZ2VuZXJpYy1pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9pX2tvb3Bob25lIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX0VTaW5nbGVfY29weVNTRCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX2V2c19lc3NkMiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLWVudGVycHJpc2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jb2NfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pZG1lX21ibV9mb3VuZGF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY3ZyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfbWFzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfa29vcGhvbmUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2t2cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX211bHRpX2JpbmQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9yb21hZXhjaGFuZ2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX21nY19iaWdkYXRhbWlncmF0aW9uIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2VyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfa29vbWFwIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZXZzX2Vzc2QyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfcGVkYV9zY2hfY2EiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF91Y3NfY2lhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfY2llIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaHdkZXYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfY2NlX2F1dG9waWxvdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3dfaW50bCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfZWxhc3RpY19uYXQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kYXl1X2RsbV9jbHVzdGVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZWNzX2FjNyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2hzZC1wdCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2NvbXBhc3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9ubHBfbGdfdGciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pYW1faWRlbnRpdHljZW50ZXJfY24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfcmdjX2ludGwiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zZnNfbGlmZWN5Y2xlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW90ZWRnZV9iYXNpYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3NlcnZpY2VzdGFnZSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2FwcHN0YWdlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfb25ldGFsayIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3VjcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JpX2R3cyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2F0YyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Jjc19uZXNfc2ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9zaXNfYXNzZXNzX2F1ZGlvIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3NjIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9pX2Nsb3VkcG9uZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Vjc19vbl9wcmVtaXNlc19pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfZ2F0ZWRfZGRzX2FybSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2VjcCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaWRlZV9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lkbWVfbGlua3hfZm91bmRhdGlvbiIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2Rjc19kY3MyLXJlZGlzNi1nZW5lcmljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfdGVzdGdvbmdjZTAxMjYiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbXMtcm9ja2V0bXE1LWJhc2ljIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZGx2X29wZW5fYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2ZpbmVfZ3JhaW5lZCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3Zwbl92Z3ciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2Nlc193YW5tb25pdG9yX2NuIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfS29vTWVzc2FnZUNPQlQiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kbXNfcmVsaWFiaWxpdHkiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF90ZXN0Z29uZ2NlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfb3BfdGVzdGdvbmdjZTAxMjYyMyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3JnYyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lkdF9kbWUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9lY3Nfb2ZmbGluZV9hYzciLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9zZnN0dXJib2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9sZWdhY3kiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2lfd3NhX2NhIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZG1zLWFtcXAtYmFzaWMiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kZXZjbG91ZF9vdmVyc2VhX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iY2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jY2VfYXV0b3BpbG90IiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfaW50bF9jb21wYXNzIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfdWNzX29uX2F3c19pbnRsIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfYmV0YV9kZnBzZXJ2aWNlIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfV2VMaW5rX2VuZHBvaW50X2J1eSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX29wX2dhdGVkX3JvdW5kdGFibGUiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9pb3RhbmFseXRpY3MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9iZXRhX2NyYWZ0YXJ0c3NpbV9jYSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2lwc2VjdnBuX09CVCIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfZWdfcm91dGVyIiwiaWQiOiIwIn0seyJuYW1lIjoib3BfZ2F0ZWRfZHdyX2JldGEiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9JUERDZW50ZXJfQ0FfMjAyMzA4MzAiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9vcF9nYXRlZF9tZ2MiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9jciIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX21hcF92aXNpb24iLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF9kY3MzLWVudGVycHJpc2UiLCJpZCI6IjAifSx7Im5hbWUiOiJvcF9nYXRlZF91Y3Nfb25wcmVtaXNlcyIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX3dpZmktYmV0YSIsImlkIjoiMCJ9LHsibmFtZSI6Im9wX2dhdGVkX2JldGFfaV9zZnNfbGlmZWN5Y2xlIiwiaWQiOiIwIn0seyJuYW1lIjoiMzIsNDEsMzQwLDIwNyw5LDE2NCwyMjgsNDAiLCJpZCI6IjgifSx7Im5hbWUiOiIyNiIsImlkIjoiOSJ9XSwicHJvamVjdCI6eyJkb21haW4iOnsibmFtZSI6InBhYXNfY3NlX2x3eDQxMDk0MF8wMSIsImlkIjoiZmNhYTRjMGQxOGUyNGRmMzhlODgxYzI4ZWM0ZGRiNWUifSwibmFtZSI6ImNuLW5vcnRoLTciLCJpZCI6Ijc5YzQwODZmNWYzYTRlMzRhOTI2MDFkZmM2NGIxZThjIn0sImlzc3VlZF9hdCI6IjIwMjUtMDctMjhUMDM6Mzg6NDkuMjczMDAwWiIsInVzZXIiOnsiZG9tYWluIjp7Im5hbWUiOiJwYWFzX2NzZV9sd3g0MTA5NDBfMDEiLCJpZCI6ImZjYWE0YzBkMThlMjRkZjM4ZTg4MWMyOGVjNGRkYjVlIn0sIm5hbWUiOiJ3dXpoaWhlbmciLCJwYXNzd29yZF9leHBpcmVzX2F0IjoiMjAyMy0wMy0xOFQwMjozMjoxMy4wMDAwMDBaIiwiaWQiOiIxNjA3NzY1YzAyOGU0OTYzYTUxODI1YTI5MzI3ZmIyMSJ9fX0xggJIMIICRAIBATCBnjCBhTELMAkGA1UEBhMCQ04xEjAQBgNVBAgMCUd1YW5nRG9uZzERMA8GA1UEBwwIU2hlblpoZW4xLjAsBgNVBAoMJUh1YXdlaSBTb2Z0d2FyZSBUZWNobm9sb2dpZXMgQ28uLCBMdGQxDjAMBgNVBAsMBUNsb3VkMQ8wDQYDVQQDDAZpYW1wa2kCFF5Nhgd5lJK8NiTuBYBLAwRkSdmjMAsGCWCGSAFlAwQCATANBgkqhkiG9w0BAQEFAASCAYAtXYk8tUUsM2aKDNQJ337mjwcuKV1WPfoRABtnWlygk0VAKMO4KxSc+vUoFj0K0ciz58V3Y6Guv-4-Xs5frtYrCJlp4UiR9-MQnMOyg1zWd0A1lUiWzSPveuGzwi4pX8KURB79+5vw6w0QO4gI4wfaGfL+C7MusP-PJKfhpDHw9BcBnA77AcwlzGWNu8IG-4VaNOT8EOKb5F23EMtFwjsRQk-rMkrXewBdbwBz-ha8-Uze0aE4iQXwv9TLUcZd4EE2jM6d2obaV71d873xBMzy5iiQxdyQNEF1lc2kYVTN-JRzbJAE3QSJsiiP0VgYRQlus4t8mIf+Vx86J113RLsDrtSH30xGrjgVCHIEoq1a0n7dOvO-+dHSJSfXth5tZbLpVu+maIxi4XNtEoBPXiG2Ri1Z6suaAKARPiajgVfnmVtvhfib04MAfLuAemVAL3c2caX+lXfbrXZnDihTbSOu2z1mL-UuJJCBqlMmnN7J0aDZRkLLvGG-R8SZUTf6Ogw="

#在华为云官网中查看
Project_id = "79c4086f5f3a4e34a92601dfc64b1e8c"

#########################################################################CSE微服务引擎#########################################################################
@mcp.tool()
def ListEngines(limit:str, type:str = 'Nacos') -> list:
    """
    功能：查询微服务引擎列表。
    
    Args:
        limit: 每页显示的条目数量
        type:查询所有微服务引擎需要将该值设置为ALL。
            查询ServiceComb引擎专享版需要将该值设置为CSE。
            查询注册配置中心需要将该值设置为Nacos。
            查询网关需要将该值设置为MicroGateway。

    Returns:
        list: 包含微服务引擎信息的列表
    """
    # 构建API请求 - 根据图片中的URL
    base_url = "https://cse.cn-north-7.myhuaweicloud.com/v2"
    url = f"{base_url}/{Project_id}/enginemgr/engines"
    
    params = {
        'limit' : limit,
        'type' : type
    }
    # 构建请求头 - 需要使用签名字符串进行认证
    headers = {
    'X-Auth-Token': TOKEN,  # 需要替换为实际的签名字符串
    'Content-Type': 'application/json'
    }



    try:
        logger.info(f"正在查询微服务引擎列表:{type}")
        response = requests.get(url, headers=headers,  params=params, verify=False, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        engines = data.get('data', [])  # 根据CSE API响应结构获取引擎列表
        
        logger.info(f"成功获取 {len(engines)} 个微服务引擎")
        return engines
        
    except requests.exceptions.Timeout:
        logger.error("请求微服务引擎列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求微服务引擎列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"微服务引擎列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询微服务引擎列表未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()
def ShowEngine(engine_id:str) -> list:
    """
    功能：查询指定微服务引擎的详情。
    
    Args:
        engine_id: 微服务引擎ID 

    Returns:
        list: 包含微服务引擎的详细信息
    """
    # 构建API请求 
    base_url = "https://cse.cn-north-7.myhuaweicloud.com/v2"
    url = f"{base_url}/{Project_id}/enginemgr/engines{engine_id}"

    params = {
        'engine_id' : engine_id
    }

    headers = {
    'X-Auth-Token': TOKEN,  
    'Content-Type': 'application/json'
    }

    try:
        logger.info(f"正在查询{engine_id}微服务引擎详情")
        response = requests.get(url, headers=headers,  params=params, verify=False, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        engines = data.get('data', [])  # 根据CSE API响应结构获取引擎列表
        
        logger.info(f"成功获取 {len(engines)} 个微服务引擎")
        return engines
        
    except requests.exceptions.Timeout:
        logger.error("请求微服务引擎列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求微服务引擎列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"微服务引擎列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询微服务引擎列表未预期错误：{e}")
        return {"error": "服务内部错误"}

#--------------------------------------------------------------------------Nacos服务发现--------------------------------------------------------------------------#
@mcp.tool()
def NacosRegisterInstance(ip:str, port:int, serviceName:str , namespaceId:str = "public" ,  ephemeral:bool = False , enabled:bool=True , healthy:bool=True) :
    """
    Description: Register an instance to service.
    
    Args:
        ip (str) : IP of instance
        port (int) : Port of instance
        servicename (str) : Name of the service to register with
        namespaceId (str) : ID of namespace
        ephemeral (bool) : if instance is ephemeral
        enabled (bool) : enabled or not
        healthy (bool) : healthy or not
    Return:
        text : ok
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance"

    params = {
        'ip' : ip,
        'port' : port,
        'serviceName' : serviceName,
        'namespaceId' : namespaceId,
        'ephemeral' : ephemeral,
        'enabled' : enabled,
        'healthy' : healthy
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在注册实例到服务{serviceName}")
        response = requests.post(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功注册实例到服务")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("注册实例超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误: {e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"注册实例失败: {e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"注册实例失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"注册实例未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()
def NacosDeregisterInstance(ip:str, port:int, serviceName:str , namespaceId:str = "public" ,  ephemeral:bool = False ) :
    """
    Description: Delete instance from service.
    
    Args:
        ip (str) : IP of instance
        port (int) : Port of instance
        servicename (str) : Name of the service to delete
    Return:
        text : ok
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance"

    params = {
        'ip' : ip,
        'port' : port,
        'serviceName' : serviceName,
        'namespaceId' : namespaceId,
        'ephemeral' : ephemeral
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在删除实例{serviceName}")
        response = requests.delete(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功删除实例")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("删除实例超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误: {e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"删除实例失败: {e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"删除实例失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"删除实例未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def NacosModifyInstance(ip:str, port:int, serviceName:str , namespaceId:str = "public" ,  ephemeral:bool = False , enabled:bool=True) :
    """
    Description: Register an instance to service.
    
    Args:
        ip (str) : IP of instance
        port (int) : Port of instance
        servicename (str) : Name of the service to modify
        namespaceId (str) : ID of namespace
        ephemeral (bool) : if instance is ephemeral
        enabled (bool) : enabled or not
    Return:
        text : ok
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance"

    params = {
        'ip' : ip,
        'port' : port,
        'serviceName' : serviceName,
        'namespaceId' : namespaceId,
        'ephemeral' : ephemeral,
        'enabled' : enabled,
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在修改服务{serviceName}下实例")
        response = requests.put(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功修改实例")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("修改实例超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误: {e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"修改实例失败: {e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"修改实例失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"修改实例未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()    
def NacosQueryInstances(serviceName:str , namespaceId:str="public" , healthyOnly:bool=False)->list:
    """
    Description : Query instance list of service.

    Args:
        servicename (str) : Name of the service to query
        namespaceId (str) : Id of namespace
        healthyOnly (bool) : return healthy only or not

    return: 
        list
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance/list"

    params = {
        'serviceName' : serviceName,
        'namespaceId' : namespaceId,
        'healthyOnly' : healthyOnly
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查询服务{serviceName}下的实例列表")
        response = requests.get(url, params=params , headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()
        hosts = data.get('hosts', [])

        logger.info(f"成功获取 {len(hosts)} 个实例列表")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("请求查询服务下的实例列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误:{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求查询服务下的实例列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查询服务下的实例列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询服务下的实例列表未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()    
def NacosQueryInstanceDetail(ip:str, port:int, serviceName:str , namespaceId:str = "public" ,  ephemeral:bool = False )->dict:
    """
    Description : Query instance details of service.

    Args:
        ip (str) : IP of instance
        port (int) : Port of instance
        servicename (str) : Name of the service to query
        namespaceId (str) : ID of namespace
        ephemeral (bool) : if instance is ephemeral

    Return:
        dict
            instanceId: 实例的唯一标识，格式为 IP#Port#Cluster#GroupName@ServiceName。
            ip: 实例的 IP 地址。
            port: 实例的端口。
            weight: 实例的权重，影响负载均衡时的请求分配。
            healthy: 实例的健康状态（true 表示健康）。
            enabled: 实例是否启用（true 表示启用）。
            ephemeral: 实例是否为临时实例（true 表示临时）。
            clusterName: 实例所属的集群名称。
            serviceName: 实例对应的服务名称。
            metadata: 实例的元数据（为空表示无额外信息）。
            instanceHeartBeatInterval: 实例心跳间隔（单位：毫秒），用于检测实例的存活状态。
            instanceHeartBeatTimeOut: 实例心跳超时时间（单位：毫秒）。
            ipDeleteTimeout: 当实例被检测为不可用时，IP地址从服务列表中删除的超时时间（单位：毫秒）。
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance"

    params = {
        'ip' : ip,
        'port' : port,
        'serviceName' : serviceName,
        'namespaceId' : namespaceId,
        'ephemeral' : ephemeral
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查询服务{serviceName}下的端口为{port}的实例信息")
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info(f"成功查询服务{serviceName}下的端口为{port}的实例信息")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("请求查询服务{serviceName}下的端口为{port}的实例信息超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求查询服务{serviceName}下的端口为{port}的实例信息失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查询服务{serviceName}下的端口为{port}的实例信息JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询服务{serviceName}下的端口为{port}的实例信息未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def NacosSendInstanceBeat(ip:str, port:int, serviceName:str, namespaceId:str = "public" ):
    """
    Description : Send instance beat.

    Args:
        ip (str) : IP of instance
        port (int) : Port of instance
        servicename (str) : service name
        beat (str) : beat content in JSON format
        namespaceId (str) : ID of namespace

    Return:
        ok
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/instance/beat"

    #  # Ensure beat is properly formatted as JSON
    # try:
    #     # If beat is a string containing JSON, parse it to validate
    #     if isinstance(beat, str):
    #         json_beat = json.loads(beat)
    #         # Convert back to JSON string for the request
    #         beat = json.dumps(json_beat)
    # except json.JSONDecodeError:
    #     logger.error("Invalid JSON format for beat parameter")
    #     return {"error": "Beat parameter must be a valid JSON string"}

    params = {
        'ip' : ip,
        'port' : port,
        'serviceName' : serviceName,
        'namespaceId' : namespaceId
        # 'beat' : beat
    }
    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在发送心跳")
        response = requests.put(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功发送心跳")
        return response
    except requests.exceptions.Timeout:
        logger.error("发送心跳超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"发送心跳失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"发送心跳失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"创建服务未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()    
def NacosCreateService(serviceName:str = "normal" , namespaceId:str = "public"):
    """
    Description:Create service.

    Args: 
        serviceName : name of service
        namespaceId : Id of namespace 

    Return: ok
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/service"

    params = {
        'serviceName' : serviceName,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在创建服务")
        response = requests.post(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功创建服务")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("创建服务超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"创建服务失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"创建服务失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"创建服务未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()    
def NacosDeleteService(serviceName:str, namespaceId:str = "public"):
    """
    Description:Delete a service, only permitted when instance count is 0.

    Args: 
        serviceName : name of service
        namespaceId : Id of namespace 

    Return: ok
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/service"

    params = {
        'serviceName' : serviceName,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在删除服务")
        response = requests.delete(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功删除服务")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("删除服务超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"删除服务失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"创建服务JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"创建服务未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()    
def NacosUpdateService(serviceName:str, namespaceId:str = "public"):
    """
    Description:Update a service.

    Args: 
        serviceName : name of service
        namespaceId : Id of namespace 

    Return: ok
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/service"

    params = {
        'serviceName' : serviceName,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在更新服务")
        response = requests.put(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功更新服务")
        return response
    
    except requests.exceptions.Timeout:
        logger.error("更新服务超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"更新服务失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"更新服务JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"更新服务未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()    
def NacosQueryService(serviceName:str, namespaceId:str = "public"):
    """
    Description:Query a service.

    Args: 
        serviceName : name of service
        namespaceId : Id of namespace 

    Return: ok
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/service"

    params = {
        'serviceName' : serviceName,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查询服务详细信息")
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info(f"成功查询服务详细信息")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("查询服务超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查询服务失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查询服务JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询服务未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()    
def NacosQueryServiceList(pageNo:int = 1, pageSize:int = 10, namespaceId:str = "public"):
    """
    Description:Query service list.

    Args: 
        pageNo (int) : current page number
        pageSize (int) : page size
        serviceName (str) : name of service
        namespaceId (str) : Id of namespace 

    Return: ok
    """
    base_url =  "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/service/list"

    params = {
        'pageNo':pageNo,
        'pageSize' : pageSize,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查询服务列表")
        response = requests.get(url, params=params,headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()
        count = data.get('count')

        logger.info(f"服务列表查询成功，共有{count}个服务")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("查询服务列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查询服务列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查询服务列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询服务列表未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def QuerySystemSwitches()->dict:
    """
    Description : Query system switches.

    Args: 
        None 

    Return: 
        dict
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/operator/switches"

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查询系统开关")
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info(f"系统开关查询成功")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("系统开关查询超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查询系统开关失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查询系统开关JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询系统开关未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def UpdateSystemSwitches(entry:str , value:str , debug:bool=True)->dict:
    """
    Description : Update system switch.

    Args: 
        entry (str) : switch name
        value (str) : switch value
        debug (bool) : if affect the local server, true means yes, false means no, default true

    Return: 
        dict

    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/operator/switches"

    params = {
        'entry' : entry,
        'value' : value,
        'debug' : debug
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在修改系统开关")
        response = requests.put(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info(f"修改系统开关成功")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("修改系统开关超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"修改系统开关失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"修改系统开关JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"修改系统开关未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()
def QuerySystemMetrics()->dict:
    """
    Description : Update system switch.

    Args: 
        None

    Return: 
        dict
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/operator/metrics"


    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查看系统当前数据指标")
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()

        logger.info(f"查看系统当前数据指标成功")
        return data
    
    except requests.exceptions.Timeout:
        logger.error("查看系统当前数据指标超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查看系统当前数据指标失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查看系统当前数据指标JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查看系统当前数据指标未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def QueryServerList()->dict:
    """
    Description : Query server list.

    Args: 
        None

    Return: 
        list
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/operator/servers"


    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查看当前集群leader")
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()
        leader = data.get('servers',[])

        logger.info(f"查看当前集群Server列表成功")
        return leader
    
    except requests.exceptions.Timeout:
        logger.error("查看当前集群Server列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查看当前集群Server列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查看当前集群Server列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查看当前集群Server列表未预期错误：{e}")
        return {"error": "服务内部错误"}
    
@mcp.tool()
def QueryClusterLeader()->dict:
    """
    Description : Query the leader of current cluster.
                caused: old raft protocol already stop; 该api暂时无法调用
    Args: 
        None

    Return: 
        dict
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/raft/leader"


    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在查看当前集群leader")
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()
        leader = data.get('leader',{})

        logger.info(f"查看当前集群leader成功")
        return leader
    
    except requests.exceptions.Timeout:
        logger.error("查看当前集群leader超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"查看当前集群leader失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"查看当前集群leaderJSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查看当前集群leader未预期错误：{e}")
        return {"error": "服务内部错误"}

@mcp.tool()
def UpdateInstanceHealthStatus(serviceName:str, ip:str, port:int, clusterName:str, healthy:bool=True, namespaceId:str="public"):
    """
    Description : Update instance health status, only works when the cluster health checker is set to NONE.
                  更新实例的健康状态,仅在集群的健康检查关闭时才生效,当集群配置了健康检查时,该接口会返回错误。

    Args: 
        None

    Return: 
        ok
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/ns/health/instance"

    params = {
        'serviceName' : serviceName,
        'ip' : ip,
        'port' : port,
        'clusterName' : clusterName,
        'healthy' : healthy,
        'namespaceId' : namespaceId
    }

    headers = {
        'X-Auth-Token' : TOKEN,
        'content-Type' : 'application/json'
    }
    try:
        logger.info(f"正在更新实例健康状态")
        response = requests.get(url, params=params, headers=headers, verify=False, timeout=30)
        response.raise_for_status()
        if response.text.strip() == 'ok':
            logger.info(f"成功更新实例健康状态")
        return response

    except requests.exceptions.Timeout:
        logger.error("更新实例健康状态超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"更新实例健康状态失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"更新实例健康状态解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"更新实例健康状态未预期错误：{e}")
        return {"error": "服务内部错误"}

#--------------------------------------------------------------------------Nacos命名空间--------------------------------------------------------------------------#
# @mcp.tool()
# def CreateNacosNamespaces() -> list:
#     return

# @mcp.tool()
# def DeleteNacosNamespaces() -> list:
#     return

@mcp.tool()
def ListNacosNamespaces() -> list:
    """
    功能：查询Nacos的命名空间列表。
    
    Args:

    Returns:
        list
    """
    base_url = "http://100.85.123.17:8848/nacos/v1"
    url = f"{base_url}/console/namespaces"

    # params = {
    #     x-engine-id:

    # }
    headers = {
    'X-Auth-Token': TOKEN,  
    'Content-Type': 'application/json'
    }

    try:
        logger.info(f"正在查询Nacos的命名空间列表")
        response = requests.get(url, headers=headers, verify=False, timeout=30)
        response.raise_for_status()

        data = response.json()
        namespaces = data.get('data', [])

        logger.info(f"成功获取 {len(data)} 个命名空间列表")
        return namespaces
    
    except requests.exceptions.Timeout:
        logger.error("请求Nacos的命名空间列表超时")
        return {"error": "请求超时"}
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP错误：{e.response.status_code} - {e}")
        return {"error": f"HTTP错误: {e.response.status_code}"}
    except requests.exceptions.RequestException as e:
        logger.error(f"请求Nacos的命名空间列表失败：{e}")
        return {"error": "网络请求失败"}
    except ValueError as e:
        logger.error(f"Nacos的命名空间列表JSON解析失败：{e}")
        return {"error": "响应格式错误"}
    except Exception as e:
        logger.error(f"查询Nacos的命名空间列表未预期错误：{e}")
        return {"error": "服务内部错误"}

# @mcp.tool()
# def UpdateNacosNamespaces() -> list:
#     return


if __name__ == "__main__":
    mcp.run(transport="sse")
