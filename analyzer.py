import openai

def analyze_resume(resume_text, job_desc):
    prompt = f"""
    You are a professional career coach AI.

    Here's a candidate's resume:
    {resume_text}

    Here's the job description:
    {job_desc}

    Please analyze the resume in detail. Your report should include:
    - Skill match percentage
    - Missing or recommended keywords
    - Suggestions for improving formatting
    - Tone and clarity insights
    - Concrete recommendations for improvement

    Format the report clearly and professionally.
    """

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5
    )
    return response.choices[0].message.content
