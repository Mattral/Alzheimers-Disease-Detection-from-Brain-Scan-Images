CSS = open("assets/styles.css", 'r').read()

IMG_BANNER = "assets/banner.png"
IMG_LOGO = "assets/logo.png"

API_URL = "https://andre-garcia-backend-clone-three.hf.space/predict"
CLASS_LABELS = ['mildly demented', 'moderately demented', 'non demented', 'very mildly demented']

SIDEBAR_TEXT_1 = """
<h1>Omdena Toronto Chapter</h1>
"""
SIDEBAR_TEXT_2 = """
<hr>
<h3 class='sidebar_h1'>Disclaimer</h3>
<h5 class='sidebar_h1'>The predictions provided by this system are for informational purposes only. Consult a healthcare professional for accurate diagnosis and advice.</h5>
"""

PROJECT_BACKGROUND = """
<h2>Project background</h2><br><p>Brain-related disorders, such as Alzheimer's disease, Parkinson's disease, and Multiple Sclerosis, are a growing global concern. As per the World Health Organization, neurological disorders are responsible for 9% of all deaths globally, and Alzheimer's and other dementias alone are among the top ten leading causes of death worldwide. With a rapidly aging population, these numbers are expected to rise significantly over the coming years. Despite significant advances in medical technology, early detection and accurate diagnosis of these conditions remain challenging. Traditionally, the diagnosis of these disorders has been based on clinical assessments and symptoms. However, these methods are often subjective and may not detect the disease until it has significantly progressed.</p>
Local Chapter Website : <a href="https://www.linkedin.com/company/omdena-toronto-chapter">Visit Site</a><br>
Dagshub Repository     : <a href="https://dagshub.com/Omdena/TorontoCanadaChapter_BrainScanImages">Visit Site</a><br>
"""

PROJECT_GOALS = f"""<h2>Project goals</h2><p>
<ul><li>Accurate Identification</li>
<li>High-Performance Metrics</li>
<li>Efficient Processing</li>
<li>Effective Training and Validation Process</li>
<li>Optimized Model</li>
<li>User-Friendly Deployment</li></ul></p>"""

PROJECT_PROBLEM = f"""
<h2>The Problem</h2> <p>The goal of this project is to leverage the power of artificial intelligence, specifically machine learning and computer vision techniques, to analyze brain scan images for the early detection and diagnosis of Alzheimer's disease, Parkinson's disease, and Multiple Sclerosis. Our aim is to create an AI model that can analyze these images, identify patterns that may be indicative of these disorders, and make predictions with high accuracy. The expectation is that such a tool could supplement existing diagnostic practices, providing a more objective and potentially earlier indication of these diseases. We believe that an accurate and efficient AI diagnostic tool can significantly improve the prognosis and quality of life for millions of patients globally.<br>
"""

PROJECT_TIMELINE = """
<h2>Project Timeline</h2>
<ol><li>Data Acquisition</li>
<li>Data Preprocessing & Exploration</li>
<li>Model Selection & Baseline Development</li>
<li>Optimizing the Model</li>
<li>Validation & Model Deployment</li>
<li>Documentation & Presentation</li></ol>
"""

ABOUT_US = """
## Introduction to Alzheimer's Disease
Alzheimer's disease (AD) is a progressive neurodegenerative disease. Though best known for its role in declining memory function, symptoms also include: difficulty thinking and reasoning, making judgements and decisions, and planning and performing familiar tasks. It may also cause alterations in personality and behavior. The cause of AD is not well understood. There is thought to be a significant hereditary component. For example, a variation of the APOE gene, APOE e4, increases risk of Alzheimer's disease.

## Why Early Detection Matters
Early detection of Alzheimer's disease is paramount because it offers the best chance for effective treatment and improved quality of life. Identifying the condition at its onset allows for timely interventions, which can slow its progression and enable individuals and their families to plan for the future. Early detection also facilitates access to support services and clinical trials, fostering hope for more effective therapies in the fight against this devastating disease.

## Purpose of the project
The purpose of this project proposal is to develop a machine learning model for the early prediction of Alzheimer's disease. Alzheimer's disease is a devastating neurodegenerative disorder that affects millions of individuals worldwide. Early detection is crucial for better patient care and the development of potential interventions. This project aims to leverage machine learning techniques to create a predictive model that can identify individuals at risk of Alzheimer's disease based on relevant data.

<br>
"""

VISUALIZATION = """
<h1 style="text-align: center; color:#FFF6F4 !important;">Visualizations developed during EDA goes here.</h1><hr>
"""

CONTRIBUTORS = """  
<h1 style="text-align: center; color:#FFF6F4;">A heartfelt thankyou to all our contributors ❤️</h1><hr>
<div style="text-align:center;">
<table>
<tr>
    <th width="20%" style="font-size: 140%;">Chapter Name</th>    
    <th width="20%" style="font-size: 140%;">Chapter Lead</th>    
</tr>
<tr>
    <td>Omdena Toronto Chapter</td>    
    <td>Kausthab Dutta Phukan</td>    
</tr>
</table>
<br>
<table>
    <tbody>
        <tr>
            <th width="20%" style="font-size: 140%;" colspan="3">Contributors</th>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>Min Htet Myet</td>
            <td>Min Htet Myet</td>
            <td>Min Htet Myet</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
    </tbody>
</table>
</div>
"""
