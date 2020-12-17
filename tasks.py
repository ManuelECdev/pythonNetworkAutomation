#- name: BUILD CONFIGS
#  buildSnippet:
#    src: "{{templateName}}.j2"
#    dest: "/etc/ansible/configs/{{idNumber}}/{{idNumber}}_{{hostname}}_{{templateName}}.cfg"

task_commonTasks_buildConfigFromTemplate = {
    "description": "BUILD CONFIGS",
    "name": "buildSnippet",
}