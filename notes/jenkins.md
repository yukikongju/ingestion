# Jenkins

- Modify Jenkins in "Configure > Mode by Jenkinsfile > Script Path: infra/jenkins/Jenkinsfile"

**Creating cron jobs for multi-branch**

- Using "Multibranch Pipeline"
    * Pros => know which branch succeeded / failed
    * Cons => no specific way to schedule cron job precisely
- Using "Freestyle Project"
    * Pros => easier to setup
    * Cons => need to duplicate job for each of the branch
