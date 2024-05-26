

test:
	@ xxd -i in.wav | > hex_xxd.txt
	@./eval.sh

run_full: compile_encode compile_decode
	@./eval.sh

wav2hex:
	@xxd in.wax > out.wav

wav2bit:
	@xxd -b in.wav > in.bits

wav2C:
	@xxd -i in.wav > hex_xxd.txt

compile_encode:
	@gcc encode.c -o encode

compile_decode:
	@gcc decode.c -o decode


clean:
	@rm -f data/*.wav.brainwire data/*.wav.copy