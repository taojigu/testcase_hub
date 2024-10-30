# Test Cases for a Login Page

## Sample pages: 

1. https://www.saucedemo.com/
   - username:standard_user
   - password:secret_sauce
2. https://opensource-demo.orangehrmlive.com/
3. https://the-internet.herokuapp.com/login
4. https://parabank.parasoft.com/parabank/index.htm
5. https://www.testyou.in/Login.aspx
6. https://reqres.in/  api test

# Test cases for https://www.saucedemo.com/

## Test Case 1: Verify login with valid credentials
- **Test Case ID**: TC_LOGIN_01
- **Priority**: High
- **Test Type**: Functional
- **Preconditions**: User must have valid credentials
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click login button.
- **Test Data**:
  - Username: `standard_user`
  - Password: `secret_sauce`
  - Homepage: https://www.saucedemo.com/inventory.html
- **Expected Result**: User is logged in successfully and redirected to the homepage.
-----
- ## Test Case 2: Verify login with unregistered username
- **Test Case ID**: TC_LOGIN_02
- **Priority**: High
- **Test Type**: Functional
- **Preconditions**: None
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter unregistered username and password.
  3. Click login button.
- **Test Data**:
  - data1: `unregisterName`
  - data2: `secret_sauce`
- **Expected Result**: display text on page,`Epic sadface: Username and password do not match any user in this service` .
---
- ## Test Case 03: Verify login with valid username and wrong password
- **Test Case ID**: TC_LOGIN_03
- **Priority**: High
- **Test Type**: Functional
- **Preconditions**: username is valid but the password is incorrect
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click login button.
- **Test Data**:
  - data1: `standard_user`
  - data2: `secret_sauce`
- **Expected Result**: display text on page,`Epic sadface: Username and password do not match any user in this service` .
---
- ## Test Case 4: Verify login in with locked out user 
- **Test Case ID**: TC_LOGIN_04
- **Priority**: High
- **Test Type**: Functional
- **Preconditions**: The username is locked.
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click login button.
- **Test Data**:
  - data1: `locked_out_user`
  - data2: `secret_sauce`
- **Expected Result**: display text on page,`Epic sadface: Username and password do not match any user in this service` .
---

- ## Test Case *: [Test case Title]
- **Test Case ID**: TC_LOGIN_**
- **Priority**: High/Medium/Low
- **Test Type**: Functional/Performance/Security
- **Preconditions**: Precondition for the test case
- **Test Steps**:
  1. Navigate to the login page.
  2. Enter valid username and password.
  3. Click login button.
- **Test Data**:
  - data1: `value1`
  - data2: `value2`
- **Expected Result**: the expected result.
---