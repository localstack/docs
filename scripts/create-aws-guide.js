const fs = require('fs')
const inquirer = require('inquirer')
const dedent = require('dedent')

const genFrontMatter = (answers) => {
    let frontMatter = dedent`---
        title: ${answers.title ? answers.title : 'Untitled'}
        linkTitle: ${answers.title ? answers.title : 'Untitled'}
        description: Get started with ${answers.title ? answers.title : '<Untitled>'} on LocalStack
        ---
        ## Introduction

        // Write a paragraph with 3-4 lines about the AWS service

        LocalStack supports ${answers.title ? answers.title : '<Untitled>'} via the Community/Pro/Team offering, allowing you to use the ${answers.title ? answers.title : '<Untitled>'} APIs in your local environment.
        The supported APIs are available on our API Coverage Page (link the page), which provides information on the extent of ${answers.title ? answers.title : '<Untitled>'} integration with LocalStack.

        ## Getting started

        This guide is designed for users new to ${answers.title ? answers.title : '<Untitled>'} and assumes basic knowledge of the AWS CLI and our awslocal wrapper script.
        
        // Provide a short tutorial to use ${answers.title ? answers.title : '<Untitled>'} with AWS CLI/awslocal

        ## LocalStack features

        // Provide a list of features that are supported by LocalStack for ${answers.title ? answers.title : '<Untitled>'}
        // You can create H2 tags for specific features and provide a short description with a code sample as well

        ## Resource Browser

        // Add a screenshot for the Resource Browser of ${answers.title ? answers.title : '<Untitled>'} if it exists
        // Provide a short description of the Resource Browser and how it can be used with ${answers.title ? answers.title : '<Untitled>'}

        The LocalStack Web Application provides a Resource Browser for ${answers.title ? answers.title : '<Untitled>'}.
        You can access the Resource Browser by opening the LocalStack Web Application in your browser, navigating to the Resources section, and then clicking on ${answers.title ? answers.title : '<Untitled>'}.

        ## Examples

        The following code snippets and sample applications provide practical examples of how to use ${answers.title ? answers.title : '<Untitled>'} in LocalStack for various use cases:

        // Link the examples from Developer Hub & Pro/Terraform/Pulumi samples
        // Provide a short description of each example

        ## Current Limitations

        // If there are any specific limitation or difference in behavior against AWS
        // Add sub-headings for each limitation and provide a short description

        ## Troubleshooting

        // Add if needed — Add sub-headings for each troubleshooting step and provide a short description
        `
    return frontMatter
}

inquirer
    .prompt([{
        name: 'title',
        message: 'What is the title of the AWS guide?',
        type: 'input',
    }])
    .then((answers) => {
        let directoryPath = answers.title
            .toLowerCase()
            .replace(/[^a-zA-Z0-9 ]/g, '')
            .replace(/ /g, '-')
            .replace(/-+/g, '-')

        const frontMatter = genFrontMatter(answers)

        const filePath = `content/en/user-guide/aws/${directoryPath}/index.md`
        fs.mkdirSync(`content/en/user-guide/aws/${directoryPath}`)
        fs.writeFile(filePath, frontMatter, (err) => {
            if (err) {
                throw err
            } else {
                console.log(`${filePath} created!`)
            }
        })
    })
    .catch((error) => {
        console.error(error)
        if (error.isTtyError) {
            console.log("Prompt was not rendered in the terminal.")
        } else {
            console.log('Error!')
        }
    })
