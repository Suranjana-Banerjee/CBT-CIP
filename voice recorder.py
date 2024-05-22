import sounddevice
from scipy.io.wavfile import write

def func(sec):
    print('Start Recording...... \n')
    recording = sounddevice.rec((sec*44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write("record.wav", 44100, recording)
    print('Stop Recording! \n')
    
func(10)