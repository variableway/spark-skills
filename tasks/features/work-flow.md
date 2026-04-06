# Workflow Skill

## Task 1: Github-workflow with gh command

- please use github cli to rewrite the current logic for better performance
- keep current solution as one alternative if gh was not install in first place

## Task 2: local workflow as an seperated skill

- keep current local workflow tracing in github-workflow-skill
- but separate the local workflow as a skill to support only local tracing without creating an github issues.

## Task 3: Install script review

Please review the skill install script,please make sure it could be install in both system level and project level

## Task 3: local work flow process is not invoked 

when github-workflow is triggered,but local workflow is not processed. The Feature should be:

1. READ the task , then trigger the github workflow, create issue, and create local tracing file
2. After AI Agent do his job, issue updated, and local tracing file updated
3. When Only trigger local workflow, the github issue is not created anymore

Verfification:
1. Update A Test GIthub Workflow Task Both Issue and local tracing file is updated
2. Update A Test Local Workflow, only local tracing file is updated
