#This file contains the tools and functions used for the healthbot application


from tavily import TavilyClient
from langchain_core.tools import tool

@tool
def web_search(question:str) -> dict:
    """This tool is used to search the web for internet searching"""
    tavily = TavilyClient()
    search = tavily.search(question)
    return search

