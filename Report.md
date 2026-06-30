CSO7024 Mid-Module Assessment Rationale
a) Approach and Git Workflow

I began by downloading the starter project, installing the required dependencies, and confirming that the existing tests passed before making any changes. I then implemented the required task priority feature and added a new automated test to verify the functionality. Throughout the development process, I used Git to record my work and created a dedicated feature branch (priority-feature) to separate the new functionality from the main branch. Once the feature had been completed and verified, I merged the feature branch back into the main branch and pushed the updated repository to GitHub.

My commit history records the main stages of development with descriptive commit messages, making it easier to understand how the project evolved. During this assignment I did not encounter a merge conflict because I was the only developer working on the repository and all changes were made within a single feature branch before being merged. By keeping development isolated and merging only after testing, conflicting changes to the same files were avoided.

b) Continuous Integration (CI) Workflow Design

I chose GitHub Actions as the Continuous Integration (CI) platform because it integrates directly with GitHub repositories and is straightforward to configure. I created a workflow file inside the .github/workflows directory that automatically runs whenever code is pushed to the repository or a pull request is created.

The workflow first checks out the repository, installs Python and the project dependencies listed in requirements.txt, and then executes the automated tests using pytest. If any test fails, GitHub Actions reports the failure immediately. If all tests pass, the workflow is marked as successful. This provides continuous verification that the application remains functional after every change without requiring manual execution of the test suite.

c) DevOps Principles Applied

This assignment demonstrates several important DevOps principles. The first is automation, as GitHub Actions automatically performs testing after each push instead of relying on manual testing. Automation improves consistency and reduces the possibility of human error.

The assignment also demonstrates fast feedback. The CI pipeline quickly reports whether new changes have introduced any problems, allowing issues to be identified and corrected early. In addition, implementing only one small feature in a dedicated branch reflects the DevOps principle of small batch sizes, making development easier to understand, review and maintain.

These practices are consistent with the CALMS model introduced in the module, particularly the principles of Automation, Measurement through automated test results, and Sharing, as GitHub provides a shared repository with a clear development history.

d) Limitations and Next Steps

Although the required functionality was successfully implemented, there are several areas that could be improved. The application currently supports only three priority levels and has a limited number of automated tests. Additional test cases, including edge cases and invalid inputs, would improve confidence in the software's reliability.

The CI workflow currently focuses only on installing dependencies and running tests. If more time were available, I would extend the workflow by adding code quality tools such as a linter and code formatter, together with additional automated checks. For the Final Project, I also expect to apply more advanced DevOps practices, including containerisation with Docker and automated deployment, allowing the complete software delivery pipeline to be automated.
