-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
SELECT tv_shows.title, SUM(tv_show_rating.rating)
FROM tv_show
INNER JOIN tv_show_rating
ON tv_show.id = tv_show_rating.show_id
GROUP BY tv_shows.title
ORDER BY rating DESC;
