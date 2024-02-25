from dotenv import load_dotenv
load_dotenv()

import deeplake
# env variable ACTIVELOOP_TOKEN must be set with your API token

# create dataset on deeplake
username = "va4az"
dataset_name = "test_dataset"
ds = deeplake.dataset(f"hub://{username}/{dataset_name}")

# create column text
ds.create_tensor('text', htype="text")

# add some texts to the dataset
texts = [f"text {i}" for i in range(1, 11)]
for text in texts:
    ds.append({"text": text})


