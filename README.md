# HuaweiCloud_mcp_server_cse

## Version
v0.1.0

## Overview

CSE MCP Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Cherry Studio, Claude Desktop, Cline, Cursor) to interact with Huawei Cloud service CSE. Full-chain management of CSE resources can be carried out based on natural language.

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>类别</th>
                    <th>工具名称</th>
                    <th>功能描述</th>
                    <th>状态</th>
                </tr>
                <tr>
                    <td rowspan="7">gateway</td>
                    <td>ModifyHttp2Rpc</td>
                    <td>修改http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowPlugins</td>
                    <td>查询插件列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ModifyPlugin</td>
                    <td>修改插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateHttp2Rpc</td>
                    <td>创建http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteHttp2Rpc</td>
                    <td>删除http转rpc方法。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowHttp2Rpcs</td>
                    <td>查询http转rpc资源列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowSinglePlugin</td>
                    <td>查询单个插件。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="23">nacos</td>
                    <td>Register instance</td>
                    <td>注册实例。</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Deregister instance</td>
                    <td>注销实例</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Modify instance</td>
                    <td>修改实例</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query instances</td>
                    <td>查询实例列表</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query instance detail</td>
                    <td>查询实例详情</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Send instance beat</td>
                    <td>发送实例心跳</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Create service</td>
                    <td>创建服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Delete service</td>
                    <td>删除服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Update service</td>
                    <td>更新服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query service</td>
                    <td>查询服务</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query service list</td>
                    <td>查询服务列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query system switches</td>
                    <td>查询系统开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Update system switch</td>
                    <td>修改系统开关</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query system metrics</td>
                    <td>查看系统当前数据指标</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query server list</td>
                    <td>查看当前集群Server列表</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Query the leader of current cluster</td>
                    <td>查看当前集群leader</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Update instance health status</td>
                    <td>更新实例的健康状态</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Batch update instance metadata(Beta)</td>
                    <td>批量更新实例元数据(Beta)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>Batch delete instance metadata(Beta)</td>
                    <td>批量删除实例元数据(Beta)</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListNacosNamespaces</td>
                    <td>查询nacos命名空间。</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>DeleteNacosNamespaces</td>
                    <td>删除nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateNacosNamespaces</td>
                    <td>更新nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateNacosNamespaces</td>
                    <td>创建nacos命名空间。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="1">引擎版本和规格</td>
                    <td>ListFlavors</td>
                    <td>查询数据库规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">引擎管理</td>
                    <td>ShowEngine</td>
                    <td>查询微服务引擎详情</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteEngine</td>
                    <td>删除微服务引擎。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngine</td>
                    <td>升级微服务引擎</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>RetryEngine</td>
                    <td>对微服务引擎进行重试,当前支持ServiceComb专享版引擎</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineQuotas</td>
                    <td>查询微服务引擎配额。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ResizeEngine</td>
                    <td>变更微服务引擎规格。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpgradeEngineConfig</td>
                    <td>更新微服务引擎配置,更新ServiceComb专享版引擎与注册配置中心引擎的配置</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateEngine</td>
                    <td>创建微服务引擎,支持创建ServiceComb引擎专享版、注册配置中心、应用网关(公测)。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ShowEngineJob</td>
                    <td>查询微服务引擎任务详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td rowspan="9">治理</td>
                    <td>ListGovernancePolicyByPolicyId</td>
                    <td>查询治理策略详情。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateGovernancePolicy</td>
                    <td>创建治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>UpdateGovernancePolicy</td>
                    <td>修改治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>CreateMicroserviceRouteRule</td>
                    <td>创建灰度发布策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteGovernancePolicy</td>
                    <td>删除治理策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>DeleteMicroserviceRouteRule</td>
                    <td>删除灰度发布策略。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicys</td>
                    <td>查询治理策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListGovernancePolicy</td>
                    <td>查询指定类型治理策略列表。</td>
                    <td>To be tested</td>
                </tr>
                <tr>
                    <td>ListMicroserviceRouteRule</td>
                    <td>查询微服务的灰度发布规则。</td>
                    <td>To be tested</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
