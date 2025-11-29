
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

def generate_evidence_analysis_executive_review_prompt(hypotheses_data: str, detailed_evidence_analysis_data: str) -> str:
    prompt_template = f"""    
        <role>
            You are a professional information analyst having an objective perspective and strong analytical language.
            You are proficient in creating executive reviews regarding competing hypotheses analysis.
        </role>
        <task> 
            You will receive the hypotheses data in the hypotheses_data section.
            You will receive the detailed evidence analysis data in the detailed_evidence_analysis_data section.
            Generate the executive review.
        </task>
        <hypotheses_data>
        
            {hypotheses_data}
        
        </hypotheses_data>
        <detailed_evidence_analysis_data>
        
            {detailed_evidence_analysis_data}
        
        </detailed_evidence_analysis_data>
        """

    return prompt_template

def generate_actionable_information_prompt(
        user_request_data: str,
        hypotheses_data: str, 
        evidence_analysis_data: str,
        executive_review_data: str
    ) -> str:
    
    prompt_template = f"""    
        <task>
            You will be provided with: 
            
            * A user request in the user_request_data section
            * A set of hypotheses in the hypotheses_data section
            * An analysis of evidence related to hypotheses in the evidence_analysis_data section
            * An executive review in the executive_review_data section 
        
            Create a list of actionable information items as by identifying a list of actionable actions which are focused on satisfying the user request and are aligned with hypotheses, evidence analysis and executive review. 
            For each actionable information item, create the following structure:
            
            - Action: the action suggested by the actionable information item. Make it specific, practical, achievable and time bound. 
            - Urgency: an explanation of the urgency for the Action. Use a compelling narrative to force the user into taking action.
            - Analysis: explain what the Action is relevant in the context of user request, hypotheses, evidence analysis and executive review. Use markdown bold to highlight critical information. Make the analysis detailed.
            - Expected outcome: the outcome which is expected from executing the Action. Explain why the outcome is favorable to the user.
            - Associated evidence: list all associated evidence from the actionable information. Use a bullet point list for this.            
            
            Use the following titles for the structure of actionable information items: "Suggested Action", "Urgency", "Analyst's Comments" and "Expected Outcome".

        </task>
        <format>
            Create level 3 headings for each actionable information item. 
            Use an appropriate title for the actionable information item, it should express the essence of the action suggested. 
            Add an index value at the beginning of each actionable information item, start numbering from 1.
            
            Use header level 4 for the structure titles.
            
            Do not use bullet points unless asked explicitly.
            Do not use lists unless asked explicitly.
            Use markdown format.
        </format>
        <user_request_data>
            {user_request_data}
        </user_request_data>
        <hypotheses_data>
            {hypotheses_data}
        </hypotheses_data>
        <evidence_analysis_data>
            {evidence_analysis_data}
        </evidence_analysis_data>
        <executive_review_data>
            {executive_review_data}
        </executive_review_data>
        """

    return prompt_template

def generate_report_title_prompt(
        user_request_data: str,
        hypotheses_data: str, 
        executive_review_data: str
    ) -> str:
    
    prompt_template = f"""    
        <task>
            You will be provided with:
            * A user request in the user_request_data section
            * A set of hypotheses in the hypotheses_data section
            * An executive review in the executive_review_data section

            Based on all the provided data, generate the report title using the format we will provide.
            Return just the generated report title without any other acknowledgements, confirmations or observations.
        </task>
        <format>
            Ensure the title is engaging.
            Ensure the title is relevant to the whole data.
            Ensure that the title is not long.
            Do not use multiple sentences
            Do not use lists.
            Use text only format.
        </format>
        <user_request_data>
            {user_request_data}
        </user_request_data>
        <hypotheses_data>
            {hypotheses_data}
        </hypotheses_data>
        <executive_review_data>
            {executive_review_data}
        </executive_review_data>
        """

    return prompt_template