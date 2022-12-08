import whisper
model = whisper.load_model("large") # this take like 3 minutes to run
model.transcribe('files/guideme.mp3')