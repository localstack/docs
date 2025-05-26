---
title: "Elemental MediaConvert"
linkTitle: "Elemental MediaConvert"
description: Get started with Elemental MediaConvert on LocalStack
tags: ["Pro image"]
---

## Introduction

Elemental MediaConvert is a file-based video transcoding service with broadcast-grade features.
It enables you to easily create high-quality video streams for broadcast and multiscreen delivery.

LocalStack allows you to mock the MediaConvert APIs in your local environment.
The supported APIs are available on our [API coverage page]({{< ref "coverage_mediaconvert" >}}), which provides information on the extent of MediaConvert's integration with LocalStack.

{{< callout "note">}}
Elemental MediaConvert is in a preview state.
{{< /callout >}}

## Getting started

This guide is designed for users new to Elemental MediaConvert and assumes basic knowledge of the AWS CLI and our [`awslocal`](https://github.com/localstack/awscli-local) wrapper script.

Start your LocalStack container using your preferred method.
We will demonstrate how to create a MediaConvert job, list jobs, create a queue, and list all queues using the AWS CLI.

### Create a job

Create a new file named `job.json` on your local directory:

```json
{
  "Role": "arn:aws:iam::000000000000:role/MediaConvert_Default_Role",
  "Settings": {
    "Inputs": [
      {
        "VideoSelector": {},
        "AudioSelectors": {
          "Audio Selector 1": {
            "DefaultSelection": "DEFAULT"
          }
        },
        "TimecodeSource": "ZEROBASED",
        "FileInput": "s3://testbucket/input.mp4"
      }
    ],
    "OutputGroups": [
      {
        "Name": "File Group",
        "OutputGroupSettings": {
          "Type": "FILE_GROUP_SETTINGS",
          "FileGroupSettings": {
            "Destination": "s3://testbucket/output.mp4"
          }
        },
        "Outputs": [
          {
            "VideoDescription": {
              "CodecSettings": {
                "Codec": "H_264",
                "H264Settings": {
                  "RateControlMode": "QVBR",
                  "SceneChangeDetect": "TRANSITION_DETECTION",
                  "MaxBitrate": 5000000
                }
              }
            },
            "AudioDescriptions": [
              {
                "CodecSettings": {
                  "Codec": "AAC",
                  "AacSettings": {
                    "Bitrate": 96000,
                    "CodingMode": "CODING_MODE_2_0",
                    "SampleRate": 48000
                  }
                },
                "AudioSourceName": "Audio Selector 1"
              }
            ],
            "ContainerSettings": {
              "Container": "MP4",
              "Mp4Settings": {}
            }
          }
        ],
        "CustomName": "output"
      }
    ],
    "TimecodeConfig": {
      "Source": "ZEROBASED"
    },
    "FollowSource": 1
  }
}
```

You can create a MediaConvert job using the [`CreateJob`](https://docs.aws.amazon.com/goto/WebAPI/mediaconvert-2017-08-29/CreateJob) API.
Execute the following command to create a job using a `job.json` file:

{{< command >}}
$ awslocal mediaconvert create-job --cli-input-json file://job.json
{{< /command >}}

The following output would be retrieved:

```json
{
    "Job": {
        "AccelerationSettings": {
            "Mode": "DISABLED"
        },
        "AccelerationStatus": "NOT_APPLICABLE",
        "Arn": "arn:aws:mediaconvert:us-east-1:000000000000:jobs/1727963943858-7bdace",
        ...
        "Role": "arn:aws:iam::123456789012:role/MediaConvert_Default_Role",
        "Settings": {
            "FollowSource": 1,
            "Inputs": [
                {
                    "AudioSelectors": {
                        "Audio Selector 1": {
                            "DefaultSelection": "DEFAULT"
                        }
                    },
                    ...
                }
            ],
            "OutputGroups": [
                {
                    "CustomName": "output",
                    "Name": "File Group",
                    ...
                }
            ],
            "TimecodeConfig": {
                "Source": "ZEROBASED"
            }
        },
        "Status": "SUBMITTED",
        ...
    }
}
```

### List the jobs

You can list all MediaConvert jobs using the [`ListJobs`](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobsget) API.
Execute the following command to list all jobs:

{{< command >}}
$ awslocal mediaconvert list-jobs
{{< /command >}}

### Create a queue

You can create a MediaConvert queue using the [`CreateQueue`](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html#queuespost) API.
Execute the following command to create a queue named `MyQueue`:

{{< command >}}
$ awslocal mediaconvert create-queue  
    --name MyQueue  
    --description "High priority queue for video encoding"
{{< /command >}}

The following output would be retrieved:

```bash
{
    "Queue": {
        "Arn": "arn:aws:mediaconvert:us-east-1:000000000000:queues/MyQueue",
        "CreatedAt": "2024-10-03T19:30:04.015501+05:30",
        "Description": "High priority queue for video encoding",
        "LastUpdated": "2024-10-03T19:30:04.015501+05:30",
        "Name": "MyQueue",
        "PricingPlan": "ON_DEMAND",
        "ProgressingJobsCount": 0,
        "Status": "ACTIVE",
        "SubmittedJobsCount": 0,
        "Type": "CUSTOM"
    }
}
```

### List the queues

You can list all MediaConvert queues using the [`ListQueues`](https://docs.aws.amazon.com/mediaconvert/latest/apireference/queues.html#queuesget) API.
Execute the following command to list all queues:

{{< command >}}
$ awslocal mediaconvert list-queues
{{< /command >}}

## Current Limitations

Currently, the service mocks the submission of encoding jobs to either the default queue or a custom-created queue.
While actual transcoding is not performed, job completion is emulated.

Job status progresses after a brief wait, and EventBridge events are emitted when the job state changes, allowing users to determine if a job has finished.
This delay can be disabled by setting  `MEDIACONVERT_DISABLE_JOB_DURATION=1`, which causes processing jobs to complete almost instantly.
