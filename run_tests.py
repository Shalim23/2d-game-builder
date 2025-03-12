import subprocess

subprocess.check_call(["cmake", "-S", "./engineTest", "-B", "engineTest/build"])
subprocess.check_call(["cmake", "--build", "engineTest/build"])
subprocess.check_call(["engineTest/build/Debug/engineTest.exe"])