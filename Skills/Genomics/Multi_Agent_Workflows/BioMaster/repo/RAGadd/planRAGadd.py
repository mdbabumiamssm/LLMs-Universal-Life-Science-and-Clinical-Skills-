from agents.Knowledge import generate_workflow_markdown, convert_markdown_to_json
if __name__ == "__main__":
    # my_content_path = "https://nf-co.re/oncoanalyser/1.0.0/"  # 可以是PDF路径或网页URL
    my_content_path = "./nature15393.pdf"  # 可以是PDF路径或网页URL
    my_openai_key = "sk-WlEo44RElYjgrTOHD9kYXTJLnkinxWqzy8Pa99sdJ9hLLnMi"
    my_openai_url = "https://sg.uiuiapi.com/v1"
    
    # 生成Markdown格式的工作流
    markdown_file = "plan_knowledge.md"
    generate_workflow_markdown(my_content_path, my_openai_key, my_openai_url, markdown_file)
    
    # 将Markdown转换为JSON并保存
    json_file = "./doc/Plan_Knowledge.json"
    convert_markdown_to_json(markdown_file, json_file)
    
    print("工作流程提取和转换完成！")