def application_tracker(applications, modification_list):
    # Create a dictionary to store the applications with their ids as keys
    application_dict = {application['id']: application for application in applications}
    
    # Iterate over the modification list
    for modification in modification_list:
        # If the modification is a key value pair
        if isinstance(modification, tuple):
            # Get the id and status from the modification
            id, status = modification
            # If the status is "delete", remove the application from the dictionary
            if status == "delete":
                application_dict.pop(id, None)
            # Otherwise, update the status of the application
            else:
                application_dict[id]['status'] = status
        # If the modification is a new application
        elif isinstance(modification, dict):
            # Assign an id to the new application
            modification['id'] = max(application_dict.keys()) + 1
            # Add the new application to the dictionary
            application_dict[modification['id']] = modification
    
    # Convert the dictionary back to a list and return it
    return list(application_dict.values())

# Define the applications and modification list
applications = [
    {"id": 101, "title": "Software Engineer", "job_description": "Design, develop, and maintain software applications in a collaborative environment.", "status": "Applied"},
    {"id": 102, "title": "Front-End Developer", "job_description": "Create visually appealing and user-friendly web interfaces using HTML, CSS, and JavaScript.", "status": "Interview Scheduled"},
    {"id": 103, "title": "DevOps Engineer", "job_description": "Implement and manage continuous integration and continuous delivery (CI/CD) pipelines.", "status": "Rejected"}
]
modification_list = [(103, "delete"),(102, "Rejected"),{'title': 'Business Development Manager', 'job_description': 'General sales activity, sales communications, and marketing support in a specified territory', 'status': 'Applied'}, {'title': 'Full Stack Engineer', 'job_description': 'Designing, developing, and maintaining complex application systems in a collaborative, team environment', 'status': 'Applied'}]

# Call the function
modified_applications = application_tracker(applications, modification_list)

# Print the modified applications
print(modified_applications)
