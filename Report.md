CSO7024 Mid-Module Assessment Rationale
a) Approach and Git Workflow

I organised my work into a series of logical steps to keep the development process structured and easy to follow.

Downloaded the starter project from Canvas.
Extracted the project files.
Installed the required Python dependencies.
Ran the existing automated tests to confirm the starter project worked correctly.
Implemented the required priority feature.
Wrote automated tests for the new functionality and confirmed that all existing tests still passed.
Initialised a local Git repository.
Made the initial commit containing the completed priority feature.
Created a feature branch (priority-feature) for subsequent development activities.
Updated the README to document the new feature.
Merged the feature branch back into the main branch.
Created and resolved a merge conflict.
Added a GitHub Actions workflow to automatically run the test suite.
Pushed the repository to GitHub and verified that the CI workflow completed successfully.
Added a task search feature as an additional enhancement in a separate commit.

Because the starter project was supplied as a ZIP archive, I extracted the project and completed the required feature before initialising Git. I therefore began version control after the implementation was complete. Following my lecturer's guidance, I retained the repository because it still demonstrates a clear and logical Git workflow, including meaningful commits, feature branching, merging, conflict resolution and Continuous Integration.
b) Continuous Integration (CI) Workflow Design

I selected GitHub Actions because it integrates directly with GitHub and is widely used in modern software development. I created a workflow that automatically runs whenever code is pushed to the repository. The workflow checks out the repository, installs the project's dependencies, and executes the automated pytest test suite.

This automation removes the need to manually execute the same verification steps after every change. Every push receives immediate feedback showing whether the application still builds successfully and whether all tests pass. A successful workflow execution in the GitHub Actions tab provides evidence that the Continuous Integration pipeline is functioning correctly and that the project remains in a working state.

c) DevOps Principles Applied

This project demonstrates several important DevOps principles introduced during the module. Automation is demonstrated through the GitHub Actions workflow, which automatically builds and tests the application whenever code is pushed. Fast feedback is achieved because test failures are reported immediately, allowing defects to be identified before further development continues.

The project also follows the principle of small batch sizes by implementing one main feature at a time and recording each logical change as an individual Git commit. Using a feature branch isolates development from the main branch until the work is complete and tested, reducing the risk of introducing unstable code. These practices align with the CALMS model by encouraging automation, collaboration through version control, continuous improvement, and maintaining a reliable software development process.

d) Limitations and Next Steps

The application remains a simple command-line task manager and currently provides only basic functionality. Although the priority feature satisfies the assessment requirements and the additional search feature improves usability, the application could be extended further. For example, future improvements could include editing existing tasks, supporting multiple search filters, adding task due dates, or providing sorting by priority and completion status.

The current automated tests mainly verify the core functionality and do not cover every possible edge case. Additional testing, including integration testing and more comprehensive validation, would further improve software quality. For the final project, I expect to build upon these DevOps practices by developing a larger application with more advanced automation, infrastructure management, and deployment techniques while continuing to use Git and Continuous Integration throughout development.
