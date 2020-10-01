# Don't Forget to Subscribe
from speedtest import Speedtest

st = Speedtest()

# print(f'''\
# %{10}s: {st.download()}
# %{10}s: {st.upload()}\
# ''' % ('Speed', 'Upload'))

print('Speed:', st.download())
print('Upload:', st.upload())

st.get_servers([])
print('Ping:', st.results.ping)