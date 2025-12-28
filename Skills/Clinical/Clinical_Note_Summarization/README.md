# Clinical Note Summarization Skill

This skill converts unstructured clinical text (dictations, rough notes) into a structured **SOAP (Subjective, Objective, Assessment, Plan)** format.

## Use Cases
- Automated medical scribing.
- Summarizing patient history for referrals.
- Standardizing electronic health records (EHR) entry.

## Files
- `prompt.md`: The system-agnostic prompt template.
- `usage.py`: A Python example showing how to load the prompt and inject data.

## Integration
This prompt is designed to be compatible with:
- **LangChain**: Use `PromptTemplate.from_file("prompt.md")`.
- **Semantic Kernel**: Can be wrapped as a Semantic Function.
- **Direct API**: Compatible with OpenAI `gpt-4`, Anthropic `claude-3-opus`, and Google `gemini-1.5-pro`.
