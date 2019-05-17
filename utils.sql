select count(y2.server_filename),sum(y2.size)>>20 sizes,y1.path from (select path from bdy where path regexp '^/.*' and isdir = 1) 
as y1 left join bdy y2 on y2.path regexp concat('^', y1.path ,'.*') where y2.isdir=0 group by y1.path order by y1.path,sizes
