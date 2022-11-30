---
title: "Transcribe"
linkTitle: "Transcribe"
categories: []
description: Get started with Amazon Transcribe on LocalStack
aliases:
  - /aws/transcribe/
---

LocalStack Community ships with an offline speech-to-text service powered by [Vosk](https://alphacephei.com/vosk/).

LocalStack requires an internet connection the first time a transcription job is created for a given language.
This is to download and cache the language model.
Subsequent transcriptions for the same language can be done offline.
Language models are around 50 MiB each and saved to the cache directory (see [Filesystem Layout]({{< ref "filesystem" >}})).

The input audio file must of single-channel PCM WAV format.

{{< alert title="Warning" color="warning">}}
This service has limited support for aarch64/Apple Silicon.
{{< /alert >}}

### Supported Languages

Currently the following langauges and dialects are supported:
- `de-DE`
- `en-GB`, `en-IN`, `en-US`
- `es-ES`
- `fa-IR`
- `fr-FR`
- `hi-IN`
- `it-IT`
- `ja-JP`
- `nl-NL`
- `pt-BR`
- `ru-RU`
- `tr-TR`
- `zh-CN`

### Examples

Create an S3 bucket and upload the audio file:

{{< command >}}
$ awslocal s3 mb s3://foo

$ awslocal s3 cp ~/example.wav s3://foo/example.wav
{{< / command >}}

Create the transcription job:

{{< command >}}
$ awslocal transcribe start-transcription-job \
    --transcription-job-name example \
    --media MediaFileUri=s3://foo/example.wav \
    --language-code en-IN
{{< / command >}}

Jobs can be listed like so:

{{< command >}}
$ awslocal transcribe list-transcription-jobs
{
    "TranscriptionJobSummaries": [
        {
            "TranscriptionJobName": "example",
            "CreationTime": "2022-08-17T14:04:39.277000+05:30",
            "StartTime": "2022-08-17T14:04:39.308000+05:30",
            "LanguageCode": "en-IN",
            "TranscriptionJobStatus": "IN_PROGRESS"
        }
    ]
}
{{< / command >}}

Once job is complete, the transcript can be retrieved from the S3 bucket:


{{< command >}}
$ awslocal transcribe get-transcription-job --transcription-job example
{
    "TranscriptionJob": {
        "TranscriptionJobName": "example",
        "TranscriptionJobStatus": "COMPLETED",
        "LanguageCode": "en-IN",
        "MediaFormat": "wav",
        "Media": {
            "MediaFileUri": "s3://foo/example.wav"
        },
        "Transcript": {
            "TranscriptFileUri": "s3://foo/7844aaa5.json"
        },
        "CreationTime": "2022-08-17T14:04:39.277000+05:30",
        "StartTime": "2022-08-17T14:04:39.308000+05:30",
        "CompletionTime": "2022-08-17T14:04:57.400000+05:30",
    }
}

$ awslocal s3 cp s3://foo/7844aaa5.json .

$ jq .results.transcripts[0].transcript 7844aaa5.json
"it is just a question of getting rid of the illusion that we are separate from nature"
{{< / command >}}
