
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/profile')
def get_profile():
    profile_data = {
        'name': 'Vamsidhar Reddy Menthem',
        'location': 'San Jose, CA',
        'education': [
            {
                'degree': 'Master of Science in Software Engineering',
                'institution': 'San Jose State University',
                'period': 'Jan 2022 - Dec 2023 (expected)',
                'coursework': ['Data Mining', 'Enterprise Software Platforms', 'Software Systems Engineering', 'Software Security Technologies']
            },
            {
                'degree': 'Bachelor of Engineering in Computer Science Engineering',
                'institution': 'K L University',
                'period': 'July 2017 - June 2021',
                'coursework': ['Object Oriented Programming', 'Data Science', 'Database Management Systems', 'Artificial Intelligence']
            }
        ],
        'technical_skills': {
            'languages_and_web': ['Python', 'Java', 'C', 'JavaScript', 'HTML', 'CSS', 'React & Spring Boot', 'NodeJS'],
            'data_science_and_ml': ['TensorFlow', 'Pandas', 'NumPy', 'Scikit-Learn', 'Seaborn', 'dplyr', 'k-means clustering', 'NLP with GPT-3', 'BERT', 'Elasticsearch'],
            'cloud_and_networking': ['AWS', 'Azure', 'Google Cloud', 'Amazon VPC', 'Azure Virtual Network'],
            'database_management': ['MySQL', 'DynamoDB', 'PostgreSQL', 'Oracle', 'Amazon Aurora'],
            'containerization_and_devops': ['Docker', 'Kubernetes', 'CI/CD', 'Jenkins', 'Terraform', 'Kafka'],
            'version_control_and_os': ['Git', 'Unix', 'Linux', 'Shell/Unix Shell scripting']
        },
        'projects': [
            {
                'name': 'Tax Bot',
                'technologies': ['AI/ML', 'Python', 'TensorFlow', 'NLP', 'Elasticsearch'],
                'description': 'A description of the Tax Bot project...'
            },
            # Additional projects...
        ]
    }
    return jsonify(profile_data)

if __name__ == '__main__':
    app.run(debug=True)
