# QA Automation Tasks

Welcome to the Device Manager project QA challenge! This document outlines your tasks for implementing a test automation framework and conducting thorough testing of the application.

## Project Overview
The Device Manager is a web application that allows users to:
- Create devices with name and IP address
- View a list of devices
- Edit existing devices
- Delete devices

The system uses MongoDB for persistent storage and Redis for caching.

## Your Tasks

### 1. Initial Setup (Required)
1. Create a pytest-based test automation framework
2. Set up necessary test fixtures for MongoDB and Redis connections
3. Implement basic test data generation helpers (optional)
4. Document your setup process and dependencies

### 2. Testing (Required)
Plan and implement test cases:
- Create separation for different test types
- Create at least a few different test cases per each test type
- If time is short, try to create a placeholder for more tests with a short description for each (optional)
- It is better to do fewer tests properly than a lot improperly
- 


### 3. Documentation and Reporting

#### Bug Reports
For any issues found, create bug reports including:
- Issue description
- Steps to reproduce
- Expected vs actual results
- Severity/priority assessment
- Supporting evidence (screenshots, logs)

#### Improvement Suggestions
Document your suggestions for:
- Application improvements
- Additional validation rules
- Error handling enhancements
- Security considerations

## Submission Requirements

1. Implement your solution in the `tests` directory
2. update the README.md with:
   - Test execution instructions
   - Any additional tools or dependencies
   - List any assumptions and prerequisites

## Tips
- Start with basic CRUD tests before moving to advanced scenarios
- Use parametrized tests for validation scenarios
- Implement proper cleanup in your test fixtures
- Document any assumptions you make
- Include error logging in your tests
- Consider test execution speed and efficiency

Good luck with your implementation! Feel free to ask any questions if you need clarification.