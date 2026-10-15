# Agentic ETL Pipeline for NCR Ride Bookings

## Overview

This project implements an agentic ETL pipeline for NCR ride booking data using PySpark, Databricks, Delta Lake, LangGraph and Microsoft Foundry.

The pipeline follows the Medallion Architecture:

- Bronze - raw ingested data
- Silver - cleaned and validated data
- Gold - analytical datasets

An agentic workflow routes user requests to ETL, quality validation, analytics and explanation capabilities.

## Technologies

- Python
- PySpark
- Databricks
- Delta Lake
- LangChain
- LangGraph
- Microsoft Foundry
- Pandas

## Architecture

```text
NCR Ride Bookings CSV
        |
        v
     Bronze
        |
        v
     Silver
        |
        v
      Gold
   /    |    \
  v     v     v
Daily Location Payment
Analytics
        |
        v
  LangGraph Supervisor
        |
   +----+----+------+
   |    |    |      |
   v    v    v      v
  ETL Quality Analytics Explain