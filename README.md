# HuaweiCloud_nacos_mcp_server

## Version
v0.1.0

## Overview
[Nacos](https://nacos.io) is an easy-to-use platform designed for dynamic service discovery and configuration and service management. It helps you to build cloud native applications and microservices platform easily.

HuaweiCloud Nacos-MCP-Server is a Model Context Protocol (Model Context Protocol) server, providing the ability for MCP clients (such as Cherry Studio, Claude Desktop, Cline, Cursor) to interact with Huawei Cloud CSE Nacos service. Full-chain management of HuaweiCloud nacos resources can be carried out based on natural language.

```markdown
1. Nacos version required  `2.x`, because of depended on the [Nacos Admin API](https://nacos.io/zh-cn/docs/open-api.html) in 2.x.
2. python version recommend upper `3.11`.
```

## Available Tools
Cover all apis, use as needed, the list and status are as follows:

<html>
    <head></head>
    <body>
        <table border="1" cellspacing="0" cellpadding="5">
            <tbody>
                <tr>
                    <th>category</th>
                    <th>tool name</th>
                    <th>function description</th>
                    <th>status</th>
                </tr>
                <tr>
                    <td rowspan="17">nacos</td>
                    <td>Register instance</td>
                    <td>Register an instance to service.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Deregister instance</td>
                    <td>Delete instance from service.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Modify instance</td>
                    <td>Modify an instance of service.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query instances</td>
                    <td>Query instance list of service.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query instance detail</td>
                    <td>Query instance details of service.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Send instance beat</td>
                    <td>Send instance beat</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Create service</td>
                    <td>Create service</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Delete service</td>
                    <td>Delete a service, only permitted when instance count is 0.</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Update service</td>
                    <td>Update a service</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query service</td>
                    <td>Query a service</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query service list</td>
                    <td>Query service list</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query system switches</td>
                    <td>Query system switches</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Update system switch</td>
                    <td>Update system switch</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query system metrics</td>
                    <td>Query system metrics</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query server list</td>
                    <td>Query server list</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Query the leader of current cluster</td>
                    <td>Query the leader of current cluster</td>
                    <td>Done</td>
                </tr>
                <tr>
                    <td>Update instance health status</td>
                    <td>Update instance health status, only works when the cluster health checker is set to NONE.</td>
                    <td>Done</td>
                </tr>
            </tbody>
        </table>
    </body>
</html>
