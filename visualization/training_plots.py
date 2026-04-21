import matplotlib.pyplot as plt

loss = [3.2,2.1,1.5,1.2,0.9]

plt.plot(loss)
plt.title("Training Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.show()