# ![cf](http://i.imgur.com/7v5ASc8.png) Lab 07: Protocols and HTTP

## Cow-say HTTP Server

**This is a Solo assignment**
<!-- short description of project -->
Today you and your partner will be building a basic HTTP server using the Python standard library.

## Specifications
<!-- Write a spefication for the features required in this lab assignment -->

### Setup
- Create a repository called `http-server`, and add your partner to the repository as a collaborator.
- Create an appropriately named branch on your `http-server` repository for today's work.
- Set up your ENV, and install a package called `cowpy`.
    - Please reference the [Package Repo](https://github.com/jeffbuttars/cowpy){:target="_blank"} for more information on using the API.
- Configure the root of your repository with the following files and directories. Thoughtfully name and organize any additional configuration or module files.
    - `README.md` - Containing good documentation for how to setup, install, and run your application
    - `.editorconfig` - Contains a standard Editor Configuration for your application (use our class standard)
    - `.gitignore` - Contains a [robust](http://gitignore.io){:target="_blank"} Git Ignore file for all relevant Python related materials
    - `test/` - Contains unit tests for your application
- Create a file called `server.py`, which will act as the entry point for your application.

### Features
- In `server.py` create the following endpoints:
    1. `GET /` - returns a valid HTML formatted response with a project description and an anchor tag which references a new request to `GET /cow`.
        - *NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose.*
        ```html
        <!DOCTYPE html>
        <html>
        <head>
            <title> cowsay </title>
        </head>
        <body>
            <header>
                <nav>
                <ul>
                    <li><a href="/cow">cowsay</a></li>
                </ul>
                </nav>
            <header>
            <main>
                <!-- project description defining how users can further interact with the application -->
            </main>
        </body>
        </html>
        ```
    2. `GET /cow?msg=text` - returns a cowpy response which correctly displays a default cow object including the `text` from your query string.
        - *NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose.*
        ```
        _____________
        < text >
        -------------
        \         __------~~-,
            \      ,'            ,
                /               \
                /                :
                |                  '
                |                  |
                |                  |
                |   _--           |
                _| =-.     .-.   ||
                o|/o/       _.   |
                /  ~          \ |
            (____\@)  ___~    |
                |_===~~~.`    |
            _______.--~     |
            \________       |
                        \      |
                    __/-___-- -__
                    /            _ \
        ```
    3. `POST /cow msg=text` - returns a cowpy response with a JSON body `{"content": "<cowsay cow>"}`
        - *NOTE: the above syntax is from the use of HTTPie. You are welcome to use whatever HTTP client you choose.*
        ```
            {
                "content": " _____________ \n< hello world >\n ------------- \n   \\         __------~~-,\n    \\      ,'            ,\n        /               \\\n         /                :\n        |                  '\n        |                  |\n        |                  |\n         |   _--           |\n         _| =-.     .-.   ||\n         o|/o/       _.   |\n         /  ~       \\ |\n       (____\\@)  ___~    |\n          |_===~~~.`    |\n       _______.--~     |\n       \\________       |\n            \\      |\n              __/-___-- -__\n             /            _ \\"
            }
        ```
    4. Both `GET` and `POST` should handle any paths that are not defined by you, and return with the appropriate `404 Not Found` response and headers.
    5. Ensure that each of your valid routes are also able to handle a malformed request, which should return a `400 Bad Request` response and headers. For example, a request to `GET /cow` which does not include a query string message is not properly formatted for your API, and should respond properly.


### Stretch Goals
- Add the ability to pass additional key/value pairs to both `GET` and `POST` requests to allow your endpoints the ability to further define the Cowpy objects. For example, change the default cow object to a dragon. If you extend your application, test your additional features as well!

### Testing
- In `test_server.py`:
    1. Create a `module` scoped fixture which will run your server on a background thred while the test suite is executing.
    1. Write test for the following functionality of your application, including separate assertions for each status code **AND** each response body (if a body exists):
        - `GET /`: `200 OK <HTML Response>`
        - `!GET /`: `400 Bad Request`

        - `GET /cow?msg=text`: `200 OK <Text Response>`
        - `GET /cow`: `400 Bad Request`
        - `GET /cow?who=dat&wat=do`: `400 Bad Request`
        - `!GET /cow?msg=text`: `405 Invalid Method`

        - `POST /cow msg=text`: `201 Created <JSON Response>`
        - `POST /cow`: `400 Bad Request`
        - `POST /cow who=this how=why`: `400 Bad Request`
        - `!POST /cow msg=text`: `405 Invalid Method`

        - `ANY /does_not_exist`: `404 Not Found`

**Your test suite should have 80% or better test coverage.**

## Submission
1. Create a pull request from your feature branch to your `master` branch.
2. In your open pull request, leave as a comment [a checklist](https://github.com/blog/1825-task-lists-in-all-markdown-documents){:target="_blank"} of the specifications, with the actual specifications you completed checked off.
3. Copy the link to your open pull request and paste it into the Canvas assignment for this day.
4. Leave any comments you may have about the assignment in the comments box. This includes any difficulties you may have had with the assignment.
5. Merge your feature branch into `master`
