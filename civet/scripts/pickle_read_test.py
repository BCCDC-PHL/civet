import pickle
import pkg_resources

spatial_translations_1 = pkg_resources.resource_filename('civet', 'data/mapping_files/HB_Translation.pkl')
pickle_objects = []
with (open(spatial_translations_1, "rb")) as openfile:
    while True:
        try:
            pickle_objects.append(pickle.load(openfile))
        except EOFError:
            break

print(*pickle_objects,sep='\n')
