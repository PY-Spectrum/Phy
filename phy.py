from quadeqn import *


class Phy:
   def __init__(self,g_const=10):
      self.g_const = g_const
   
   def FreeFall_time(self,height,u=0):
      global freefall_time   
      if u==0:
         freefall_time = ((2*height)/self.g_const)**0.5
      elif u!=0 and u > 0:
         freefall_time = eqn(self.g_const/2,u,height)
      else:
         freefall_time = "initial velocity should not be negative"

      return freefall_time

   def FreeFall_velocity(self,height,u=0):
      global freefall_velocity
      if u==0:
         freefall_velocity = (2*height*self.g_const)**0.5
      elif u!=0 and u>0:
         freefall_velocity = (2*self.g_const*height+u**2)**0.5
      else:
         freefall_velocity = "initial velocity should not be negative"

      return freefall_velocity

   def VerticalMotion_maxheight(self,u=1):
      global verticalmotion_maxheight
      if u==0:
         verticalmotion_maxheight = "initial velocity can not be 0"
      elif u!=0 and u>0:
         verticalmotion_maxheight = ((u**2)/(2*self.g_const))**0.5
      else:
         verticalmotion_maxheight = "initial can not be negative"

      return verticalmotion_maxheight

   def VerticalMotion_time(self,u=1):
      global verticalmotion_time

      if u==0:
         verticalmotion_time = "initial velocity can not be 0"
      elif u!=0 and u>0:
         verticalmotion_time = (2*u)/self.g_const
      else:
         verticalmotion_time = "initial velocity can not be negative"

   def ProjectileMotion_time(self,u=1,angle_of_projection=90):
      global projectile_time
      angle_rad = math.radians(angle_of_projection)
      if u==0:
         projectile_time = "initial velocity can not be 0"
      elif u!=0 and u>0:
         projectile_time = (2*u*math.sin(angle_rad))/(self.g_const)
      else:
         projectile_time = "initial velocity can not be negative"

      return projectile_time

   def ProjectileMotion_maxheight(self,u=1,angle_of_projection=90):
      global projectile_maxheight
      angle_rad = math.radians(angle_of_projectile)
      if u==0:
         projectile_maxheight = "initial velocity can not be 0"
      elif u!=0 and u>0:
         projectile_maxheight = ((u**2)*math.sin(angle_rad))/(self.g_const)
      else:
         projectile_maxheight = "initial velocity can not be negative"

      return projectile_maxheight
   
   def Projectile_range(self,u=1,angle_of_projection=90):
      global projectile_range
      angle_red = math.radians(angle_of_projection)
      if u == 0:
         projectile_range = "initial velocity can not be 0"
      elif u!=0 and u>0:
         projectile_range = (2*(u**2)*math.sin(angle_of_projection)*math.cos(angle_of_projectile))/self.g_const
      else:
         projectile_range = "initial velocity can not be negavite"

      return projectile_range

   def resolution_2d(vector_magnitude = 1,angle=45):
      angle_wrt_x = math.radians(angle)
      vector_x = vector_magnitude*math.cos(angle_wrt_x)
      vector_y = vector_magnitude*math.sin(angle_wrt_x)

      return (vector_x,vector_y)

   def dot_product(vector_1,vector_2):
      global return_dot
      if len(vector_1) > 3 or len(vector_2)>3 or type(vector_1) != type([]) or type(vector_1) !=type([]):
         return_dot = "Enter valid datatypes and make sure they are all of list datatype."
      count_1 = 0
      count_2 = 0
      for i in vector_1:
         count_1+=1
         for j in vector_2:
            count_2+=1
            if count_1 == count_2:
               return_dot += i*j
            else:
               pass

      return return_dot

   def cross_product(self,vector_1,vector_2):
      global return_cross
      if len(vector_1) > 3 or len(vector_2)>3 or type(vector_1) != type([]) or type(vector_1) !=type([]):
         return_cross = "Enter valid datatypes and make sure they are all of list datatype."
      possible_vector_unit = ["i","j","k"]
      vector_1_dict = dict()
      vector_2_dict = dict()
      count_1 = 0
      count_2 = 0
      i_endval = []
      j_endval = []
      k_endval = []
      for i in vector_1:
         vector_1_dict[possible_vector_unit[count_1]] = i
         count_1+=1
      for j in vector_2:
         vector_2_dict[possible_vector_unit[count_2]] = i
         count_2+=1

      for i in vector_1_dict:
         for j in vector_2_dict:
            if i=="i" and j=="j":
               k_endval.append(vector_1_dict[i]*vector_2_dict[j])
            elif i =="i" and j=="k":
               j_endval.append(-1*vector_1_dict[i]*vector_2_dict[j])
            elif i=="j" and j=="i":
               k_endval.append(-1*vector_1_dict[i]*vector_2_dict[j])
            elif i=="j" and j=="k":
               i_endval.append(vector_1_dict[i]*vector_2_dict[j])
            elif i=="k" and j=="i":
               j_endval.append(vector_1_dict[i]*vector_2_dict[j])
            elif i=="k" and j=="j":
               i_endval.append(vector_1_dict[i]*vector_2_dict[j])

      i_finalval = 0
      j_finalval = 0
      k_finalval = 0

      for i in i_endval:
         i_finalval+=i
      for j in j_endval:
         j_finalval+=j
      for k in k_endval:
         k_finalval+=k

      if j_finalval>0:
         j_finalval = "+ "+str(j_finalval)
      if k_finalval>0:
         k_finalval = "+ "+str(k_finalval)

      return_cross = str(i_finalval)+"i "+str(j_finalval)+" j "+str(k_finalval)+" k "

      return return_cross
   
               
               
               
               
               
