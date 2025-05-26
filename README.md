# MCP Server FDC

A Python implementation of a server for the Model Context Protocol (MCP) focusing on Forecourt Device Controller (FDC) functionality for tank delivery data.

## Overview

This project provides a Model Context Protocol implementation for accessing and manipulating tank delivery data from Forecourt Device Controllers. It leverages the MCP Python SDK to expose tools that can be used by AI assistants to interact with fuel tank monitoring systems.

## What is Model Context Protocol (MCP)?

The Model Context Protocol is an open standard that enables developers to build secure, two-way connections between their data sources and AI-powered tools. Created by Anthropic, MCP standardizes how AI systems interact with external tools and data sources, similar to how the Language Server Protocol standardized programming language support across development tools.

Key MCP concepts:
- **MCP Servers**: Expose data and functionality (like our FDC tank data) through a standardized interface
- **MCP Clients**: AI applications that connect to MCP servers to utilize those tools
- **Tools**: Functions that can be invoked by AI systems (like our tank delivery data retrieval functions)
- **Resources**: Static or dynamic data that can be accessed by AI systems
- **Prompts**: Pre-defined text that can guide AI interactions

MCP enables AI systems to:
- Access real-time data directly from source systems
- Perform actions based on that data
- Maintain context across different tools and datasets

## Features

- **FDC Tools**: 
  - Retrieve tank delivery data for all tanks
  - Retrieve tank delivery data for specific tanks by device ID
- **Asynchronous Implementation**: Service calls are implemented with async/await pattern for better performance
- **Type Safety**: Pydantic models ensure proper data validation and serialization
- **MCP Standard Compliance**: Built with the official MCP Python SDK

- Retrieve tank delivery data for all tanks
- Retrieve tank delivery data for specific tanks by device ID
- Pydantic models for proper type validation and serialization
- Asynchronous service implementation for better performance

## Project Structure# FdcPythonMcpServer
