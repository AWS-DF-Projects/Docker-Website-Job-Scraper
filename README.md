## Docker-Website-Job-Scraper

This project wasn’t necessarily the best approach for the task at hand, but it was built to help me dig through the internet for tech jobs without having to manually check every site. With this setup, the EC2 instance does the searching and just gives me the results.

Eventually, the idea is to send the scraped jobs to a simple job website for me to browse and also get a daily email summary with the results.

> Please note this is only partially built. One of the main reasons is the quality of job sites I tested the jobs were too few and not really relevant to me. I like my projects to have real-world purpose, and while the sites didn’t work out, I wanted to show the architecture and flow because it does work if you feed in better data sources.

![image](https://github.com/user-attachments/assets/cbc2b83d-6530-4eba-ae02-9db21ee6a4f1)

Here’s how it works:
- A CRUD trigger or EventBridge rule invokes a Lambda.
- That Lambda starts up an AMI (with Docker pre-installed) and injects the user data script.
- The user data installs permissions, pulls Docker images, and runs two scraper jobs in containers.
- The scraped job data is saved to the attached EBS volume.
- (Not yet built) At the end, the EC2 instance should send the job list to an S3 path like /job-images for a static website to display.
- It also plans to email the user a summary with a link to the site.
- After that, the EC2 instance shuts itself down to save costs and wait for the next daily EventBridge trigger.

After testing this, I realised this setup doesn’t really suit my needs. Most of the jobs I’m interested in actually land in my email inbox so I’ve started building a new version of this system that scrapes my emails instead. It’ll extract job info and links from there, and eventually get job data from sites like LinkedIn or Indeed based on those leads.

That project is in the works: [Link to that GH repo once it's live]
