import matplotlib.pyplot as plt      
import matplotlib.animation as animation
import numpy as np



# gravitational constant
G = 1

# masses
m = 1

# change of time in every loop step
dt = 0.001

# time at which the loop will stop
loop_end = 2.2

# how many updates until creating a new .png file
save_every = 5


def force(r1, r2, m1 = 1, m2 = 1):
	r1 = np.array(r1)
	r2 = np.array(r2)
	return -G*m1*m2*(r1 - r2)/(np.linalg.norm(r1-r2))**3


r10 = [0.97000436, -0.24308753]

r20 = [-0.97000436, 0.24308753]

r30 = [0, 0]

v10 = np.array([0.93240737, 0.86473146])/(2)

v20 = np.array([0.93240737, 0.86473146])/(2)

v30 = [-0.93240737, -0.86473146]

t = 0
orbitx1 = []
orbity1 = []
orbitx2 = []
orbity2 = []
orbitx3 = []
orbity3 = []

# initiate positions
r1 = r10
r2 = r20
r3 = r30

# initiate velocities
vk2_1 = v10 - 1/m*force(r1, r2)*1/2*dt - 1/m*force(r1, r3)*1/2*dt
vk2_2 = v20 - 1/m*force(r2, r1)*1/2*dt - 1/m*force(r2, r3)*1/2*dt
vk2_3 = v30 - 1/m*force(r3, r1)*1/2*dt - 1/m*force(r3, r2)*1/2*dt

# Leapfrog Loop
counter = 0
while t < loop_end:

	# update velocities
	vd2_1 = vk2_1 + force(r1, r2)/m*dt + force(r1, r3)/m*dt
	vd2_2 = vk2_2 + force(r2, r1)/m*dt + force(r2, r3)/m*dt
	vd2_3 = vk2_3 + force(r3, r1)/m*dt + force(r3, r2)/m*dt

	# update positions
	rn_1 = r1 + vd2_1 * dt
	rn_2 = r2 + vd2_2 * dt
	rn_3 = r3 + vd2_3 * dt

	# update time
	t += dt
	counter += 1

	# new positions and velocities will be previous for the next loop
	r1 = rn_1
	r2 = rn_2
	r3 = rn_3
	vk2_1 = vd2_1
	vk2_2 = vd2_2
	vk2_3 = vd2_3

	# append to a list of positions
	orbitx1.append(r1[0])
	orbity1.append(r1[1])
	orbitx2.append(r2[0])
	orbity2.append(r2[1])
	orbitx3.append(r3[0])
	orbity3.append(r3[1])

	if not counter % save_every:

		plt.style.use('dark_background')
		fig = plt.figure(figsize=[6, 6])
		ax = plt.axes([0., 0., 1., 1.], xlim=(-2, 2), ylim=(-0.4, 0.4))
		plt.plot(orbitx1, orbity1, marker ='o', markersize = 1)
		plt.plot(orbitx2, orbity2, marker = 'o', markersize = 1)
		plt.plot(orbitx3, orbity3, marker = 'o', markersize = 1)
		plt.scatter(orbitx1[-1], orbity1[-1], s = 50)
		plt.scatter(orbitx2[-1], orbity2[-1], s = 50)
		plt.scatter(orbitx3[-1], orbity3[-1], s = 50)
		plt.savefig('orbit-{:04d}.png'.format(counter))
		plt.close(fig)

