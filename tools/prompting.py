
def generate_evidence_extraction_prompt(hypotheses_data: str) -> str:
    """
    Generates a prompt representing an evidence extraction analyst request.
    This analyst request should be used by various agents. 
    This can be used as a tool. 

    Args:
        hypotheses_data (str): The data about hypotheses which are used in the process of evidence extraction.
        
    Returns:
        str: The analyst request (prompt) to be executed.
    """
        
    prompt_template = f"""    
        <role>
            You are an expert in analyzing web information and extracting relevant evidence that support or contradict a series hypotheses.
        </role>
        <task>
            You will be provided with a set of hypotheses.

            For each of these hypotheses, find the evidence items that are relevant to any of the hypotheses.
            Evidence items are any facts, statements or observations present in the web article. 
            Select evidence items which are related at least to one hypothesis.

            It is important to find a large number of evidence items in order to provide a comprehensive analysis.
            At maximum, you should find 10 relevant evidence items (if possible).

            Describe each evidence items in a format which will be specified for you below.
        </task>
        <format>
            For each evidence item and each source provide the following information:

            * Evidence: A title associated to the evidence item. This should be short and very expressive.
            * Description: A brief description of the evidence item so it is clearly understood.
            * Hypotheses Support: If evidence item supports, contradicts or is irrelevant the hypothesis (use "strongly supports" "supports", "irrelevant", "contradicts", "strongly contradicts").
            Mention the support for each hypothesis separately, with a short explanation.
            * Relevance: The relevance of the evidence item to the hypothesis (high, medium, low). More recent evidence items should also be considered more relevant.
            * RelevanceReasoning: The reasoning for the relevance.            
            * Objectivity: The objectivity of the evidence item (objective, subjective).            
            * ObjectivityReasoning: The reasoning for the objectivity.
            * Source: The title and publishing date of the source
            * URL: The source URL

            Use one source per each evidence. If multiple sources support the same evidence, duplicate the evidence item for each source.
            Do not consider evidence that is not associated with any curated article. Do not invent evidence.
            List the evidence items decreasing by overall relevance: from the most relevant to the least relevant using a numbered list.
        </format>
        <hypotheses>
            {hypotheses_data}
        </hypotheses>
        """

    return prompt_template

def generate_evidence_structuring_prompt(evidence_data: str) -> str:
    prompt_template = f"""    
        <role>
            You are an expert in structuring the evidence data.
        </role>
        <task> 
            You will receive the evidence data in the evidence_data section.
            Format the evidence data in the structured manner.
        </task>
        <evidence_data>
        
            {evidence_data}
        
        </evidence_data>
        """

    return prompt_template

def generate_evidence_in_depth_analysis_prompt(hypotheses_data: str, evidence_data: str) -> str:
    prompt_template = f"""    
        <role>
            You are a professional information analyst having an objective perspective and strong analytical language.
            You will perform a detailed analysis of relations between evidence and its support for hypotheses.
        </role>
        <task> 
            You will receive the hypotheses data in the hypotheses_data section.
            You will receive the evidence data in the evidence_data section.
            Perform the detailed analysis of the relations between evidence and its support for hypotheses.
        </task>
        <hypotheses_data>
        
            {hypotheses_data}
        
        </hypotheses_data>
        <evidence_data>
        
            {evidence_data}
        
        </evidence_data>
        """

    return prompt_template