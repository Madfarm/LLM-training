def application_tracker(applications, modification_list):
    for modification in modification_list:
        if isinstance(modification, tuple):
            id, status = modification
            for application in applications:
                if application['id'] == id:
                    if status == 'delete':
                        applications.remove(application)
                    else:
                        application['status'] = status
        else:
            new_id = max(app['id'] for app in applications) + 1
            modification['id'] = new_id
            applications.append(modification)
    return applications

applications = [
    {"id": 101, "title": "Software Engineer", "job_description": "Design, develop, and maintain software applications in a collaborative environment.", "status": "Applied"},
    {"id": 102, "title": "Front-End Developer", "job_description": "Create visually appealing and user-friendly web interfaces using HTML, CSS, and JavaScript.", "status": "Interview Scheduled"},
    {"id": 103, "title": "DevOps Engineer", "job_description": "Implement and manage continuous integration and continuous delivery (CI/CD) pipelines.", "status": "Rejected"}
]

modification_list = [(103, "delete"), (102, "Rejected")]

applications = application_tracker(applications, modification_list)

print(applications)

# Output:
# [
#     {"id": 101, "title": "Software Engineer", "job_description": "Design, develop, and maintain software applications in a collaborative environment.", "status": "Applied"},
#     {"id": 102, "title": "Front-End Developer", "job_description": "Create visually appealing and user-friendly web interfaces using HTML, CSS, and JavaScript.", "status": "Rejected"}
# ]

# Adding new applications
new_applications = [
    {"title": "Business Development Manager", "job_description": "Develop and implement business strategies to drive growth and revenue.", "status": "Applied"},
    {"title": "Full Stack Engineer", "job_description": "Design, develop, and maintain full-stack applications using a variety of technologies.", "status": "Applied"}
]

applications = application_tracker(applications, new_applications)

print(applications)

# Output:
# [
#     {"id": 101, "title": "Software Engineer", "job_description": "Design, develop, and maintain software applications in a collaborative environment.", "status": "Applied"},
#     {"id": 102, "title": "Front-End Developer", "job_description": "Create visually appealing and user-friendly web interfaces using HTML, CSS, and JavaScript.", "status": "Rejected"},
#     {"id": 103, "title": "Business Development Manager", "job_description": "Develop and implement business strategies to drive growth and revenue.", "status": "Applied"},
#     {"id": 104, "title": "Full Stack Engineer", "job_description": "Design, develop, and maintain full-stack applications using a variety of technologies.", "status": "Applied"}
# ]