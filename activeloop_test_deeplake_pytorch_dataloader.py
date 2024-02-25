

from dotenv import load_dotenv
load_dotenv()

import deeplake

# create dataset on deeplake
username = "va4az"
dataset_name = "test_dataset"
ds = deeplake.dataset(f"hub://{username}/{dataset_name}")

# create PyTorch data loader
batch_size = 3
train_loader = ds.dataloader()\
            .batch(batch_size)\
            .shuffle()\
            .pytorch()

# loop over the elements
for i, batch in enumerate(train_loader):
    print(f"Batch {i}")
    samples = batch.get("text")
    for j, sample in enumerate(samples):
        print(f"Sample {j}: {sample}")
    print()
    pass


