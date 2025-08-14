# Copilot Instructions

This document provides guidance for GitHub Copilot to generate consistent, high-quality code in this repository.

---

## Purpose

The purpose of this file is to guide GitHub Copilot when suggesting code, ensuring that generated code:

- Follows the repository’s coding standards
- Adheres to best practices
- Matches the project's architectural patterns
- Aligns with security and performance guidelines

---

## General Guidelines

1. **Language & Framework**
   - Use the primary language(s) of the repository: **JavaScript/TypeScript, Python**
   - Follow the standard framework patterns already in use (React, Express, etc.)

2. **Code Style**
   - Follow [ESLint](https://eslint.org/) rules for JavaScript/TypeScript.
   - Use Prettier formatting style.
   - Ensure code is readable and maintainable.
   - Prefer descriptive variable and function names.

3. **Documentation**
   - Write concise and clear comments for complex logic.
   - For functions, include JSDoc or Python docstrings with parameter and return type descriptions.

4. **Error Handling**
   - Always handle errors gracefully and provide meaningful error messages.
   - Avoid silent failures.

5. **Security**
   - Never hardcode secrets, credentials, or API keys.
   - Use environment variables for sensitive data.

6. **Performance**
   - Avoid unnecessary loops and computations.
   - Optimize database queries.
   - Use async/await for asynchronous operations.

---

## Project-Specific Rules

1. **React Components**
   - Use functional components and React Hooks.
   - Keep components small and focused.
   - Use TypeScript interfaces or PropTypes for props validation.

2. **API Development**
   - Follow RESTful API design principles.
   - Validate incoming request data using the existing validation middleware.
   - Always sanitize user input to prevent injection attacks.

3. **Testing**
   - Write unit tests for all new features.
   - Follow existing test patterns using Jest or Pytest.
   - Ensure tests are deterministic and isolated.

4. **Git Commit Messages**
   - Use descriptive commit messages.
   - Follow the convention: `<type>(<scope>): <description>`  
     Example: `feat(api): add user authentication endpoint`

---

## Example Prompts for Copilot

When writing code with Copilot in this repo, use prompts like:

- *"Create a React functional component with TypeScript props for a user profile card."*
- *"Write an Express.js route to fetch all orders with pagination and sorting."*
- *"Add a Jest unit test for the calculateTotalPrice function in utils/price.js."*
- *"Generate a Python function to process uploaded CSV files and return a summary."*

---

## Do Not

- Generate code in a different language unless explicitly required.
- Write code without proper error handling.
- Introduce dependencies without team approval.
- Bypass security best practices.

---

## References

- [Repository README.md](./README.md)
- [Coding Standards](./CODING_STANDARDS.md)
- [Security Guidelines](./SECURITY.md)
- [Contribution Guide](./CONTRIBUTING.md)
