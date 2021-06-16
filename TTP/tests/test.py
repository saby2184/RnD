import racepretextproc
from racepretextproc.visualization import visualize
from racepretextproc.noise_remove import noise_remove
from racepretextproc.lemetstemtoken import lemetstemtoken
from racepretextproc.normalization import normalization
text = r'Listen waitng on a port/ip address combination. By using this variable multiple times, mosquitto can listen on more ' \
       r'than one port. If this variable is used and neither bind_address nor port given, then the default listener ' \
       r'will not be started. The port number to listen on must be given. Optionally, an ip address or host name may ' \
       r'be supplied as a second argument. In this case, mosquitto will attempt to bind the listener to that address ' \
       r'and so restrict access to the associated network and interface. By default, mosquitto will listen on all ' \
       r'interfaces. Note that for a websockets listener it is not possible to bind to a host name. listener ' \
       r'port-number '

# wc = visualize.WordCloud(max_words=100);
# wc.show(text)
#
# visualize.FrequencyDist.show(text, min_length=3,nof_large_words=50)


# text="I love NLP #Check $234 21/25 as23"
# text_proc=noise_remove.textpreprocessor(text)
# # processed_text = text_proc.remove_noise([text_proc.lower])
# processed_text = text_proc.remove_noise(remove_stop_words=False)
# print(processed_text)

#
# lemstemObj = lemetstemtoken.lemetization_stemming_tokenization(text);
# print(lemstemObj.lemet_stem_token(do_stem=True))

# print(normalization.normalization(text).normalizmain())
print(racepretextproc.process(text))
