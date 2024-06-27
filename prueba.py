import numpy as np
import random

loser_selection= ['Jorge', 'pringado', 'niño de UNICEF','champ']
hunger_selection = [1,5,10]
girlfriend_selection = ['Alba', 'Pringui', 'Chiteki', 'THE MOST Absolute Bestest GF ever']
current_task_selection = ['becoming a Rustacean', 'embodying Ferris', 'waiting to see The Most Absolute Bestest GF ever']
proof_of_wisdom = np.power(2,3)

print("""
Here is your personalized, RANDOM, birthday celebration. It has been made with Made with loooots of love and loooots of free time ;)
      Hey hey hey, what is UP, DOWN, SIDE TO SIDE, {} ??
      I hope that your hard work dedicated to {} is going EXTREMELY well.
      Yeah, so... you may know that I, {},  am reeeeally excited to see you today of ALL days ;)
      (I mean, I am excited to see you all days, but it was for the sake of this masterpiece. Don't think too highly of yourself...) 
      Despite your mental age of {}, I wish you a great 23rd birthday (... again).
      (Jeeeehzuzzzz, looks like this woman has far too much free time on her hands...)
      
      Regardless... Espero que te haya entretenido ligeramente esta pequeña sorpresa, tal y como me ha entretenido a mí el hacerla durante un par de minutos ajajajaj.
      
      Y con TODO lo anterior solo me queda decir que: {}. Ahá, como lo oyes. Lo he hecho con NUMPY! ;) Aaadios
""".format(random.choice(loser_selection), random.choice(current_task_selection), random.choice(girlfriend_selection), random.choice(hunger_selection),proof_of_wisdom))
