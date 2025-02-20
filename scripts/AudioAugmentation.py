import os
import ffmpeg
import csv

def trim_audio(input_file, output_file, start_duration, end_duration):
    """
    Trims the audio by removing specified durations from the beginning and end.

    Args:
    input_file: Path to the input audio file.
    output_file: Path to save the trimmed audio file.
    start_duration: Duration to trim from the beginning (in seconds).
    end_duration: Duration to trim from the end (in seconds).
    """
    # Get audio duration using ffprobe
    try:
        probe_result = ffmpeg.probe(input_file)
    except ffmpeg.Error as e:
        print(f"Error getting audio duration: {e}")
    duration = float(probe_result['format']['duration'])

    # Calculate trim durations
    trim_start = start_duration
    trim_end = duration - end_duration

    # Execute ffmpeg command to trim the audio
    try:
        (
            ffmpeg
            .input(input_file)
            .audio.filter(r"atrim",trim_start,trim_end)
            .output(output_file)
            .run(overwrite_output=True, capture_stderr=True, capture_stdout=True) # Capture stdout and stderr for debugging
        )
        print(f"Successfully trimmed audio from {input_file} to {output_file}")
    except ffmpeg.Error as e:
        print(f"Error trimming audio: {e.stderr.decode()}")




if __name__ == "__main__":
    # Example usage
    input_file = ""
    output_file = ""
    start_duration = 30  
    end_duration = 60 

    trim_audio(input_file, output_file, start_duration, end_duration)