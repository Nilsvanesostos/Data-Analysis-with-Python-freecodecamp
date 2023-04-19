import numpy as np

def calculate(list):

  if len(list) !=9:
    raise ValueError('List must contain nine numbers.')
    
  m=np.array([[list[0],list[1],list[2]],[list[3],list[4],list[5]],[list[6],list[7],list[8]]])
                                                            
  
  calculations= {
  'mean': [[np.mean(m[:,:1]), np.mean(m[:,1:2]), np.mean(m[:,2:3])], [np.mean(m[0]), np.mean(m[1]), np.mean(m[2])], np.mean(m)],
  'variance': [[np.var(m[:,:1]), np.var(m[:,1:2]), np.var(m[:,2:3])], [np.var(m[0]), np.var(m[1]), np.var(m[2])], np.var(m)],
  'standard deviation': [[np.std(m[:,:1]), np.std(m[:,1:2]), np.std(m[:,2:3])], [np.std(m[0]), np.std(m[1]), np.std(m[2])], np.std(m)],
  'max': [[np.max(m[:,:1]), np.max(m[:,1:2]), np.max(m[:,2:3])], [np.max(m[0]), np.max(m[1]), np.max(m[2])], np.max(m)],
  'min': [[np.min(m[:,:1]), np.min(m[:,1:2]), np.min(m[:,2:3])], [np.min(m[0]), np.min(m[1]), np.min(m[2])], np.min(m)],
  'sum': [[np.sum(m[:,:1]), np.sum(m[:,1:2]), np.sum(m[:,2:3])], [np.sum(m[0]), np.sum(m[1]), np.sum(m[2])], np.sum(m)]
}


  return calculations
