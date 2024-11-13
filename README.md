
# Multi-Language Morse Code Converter
 

## Abstract
Morse code, a historic method of encoding text into a sequence of dots and dashes, is still used today in various forms, such as digital secret messaging and evading censorship. However, translating Morse code requires skill or an interpreter, and currently, Morse code only supports the Latin alphabet, limiting its accessibility across languages. This project, the Speech-to-Morse Code Generator, bridges this gap by enabling conversion from spoken input in multiple languages into Morse code and vice versa, improving accessibility and usability for non-English speakers.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Encrypt Function](#encrypt-function)
  - [Decrypt Function](#decrypt-function)
- [Results](#results)
- [Conclusion](#conclusion)
- [References](#references)

## Introduction
Morse code encodes text as standardized sequences of short and long signals (dots and dashes), traditionally supporting only the 26 letters of the English alphabet. This project extends Morse code use by converting spoken input in various languages to Morse code and translating Morse back into any chosen language. It eliminates the need for typing or English language knowledge, creating a versatile, language-inclusive Morse code communication system.

## Features
- **Encrypt spoken text** in multiple languages into Morse code.
- **Decrypt Morse code audio** back into text in any desired language.
- **Audio feedback** for both Morse code and translated text.
- **Save Morse code audio** to `.mp3` for sharing or storage.

## Requirements
To run this project, ensure the following dependencies are installed:
- **Python** 2.6, 2.7, or 3.3+
- **SpeechRecognition** 3.8.1 – A speech recognition library supporting various APIs.
- **PyAudio** 0.2.11+ – Enables cross-platform audio recording and playback.
- **googletrans** 3.0.0 – Interface for Google Translate API to handle translations.
- **pyttsx3** 2.90 – Text-to-speech library that functions offline.
- **gTTS** – Google Text-to-Speech library for converting text to speech.
- **playsound** 1.3.0 – Simple sound playback module.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-to-morse-generator.git
   cd speech-to-morse-generator

