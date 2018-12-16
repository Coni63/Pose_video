CALL activate machine_learning
python video_extractor.py
python render.py
python video_writer.py
ffmpeg -i F:/data/test/output.avi -i test.mp3 -codec copy -shortest output.avi