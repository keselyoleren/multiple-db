** concept penggunaan multiple database **

*** Config Multiple database ***

```
DATABASES = {
    'default': {
        'ENGINE'    : config("DB1_CONNECTION", default='django.db.backends.postgresql_psycopg2'),
        'USER'      : config('DB1_USER', default='root'),
        'NAME'      : config('DB1_NAME'),
        'PASSWORD'  : config('DB1_PASSWORD', default=''),
        'HOST'      : config('DB1_HOST', default='localhost'),
        'PORT'      : config('DB1_PORT', default='5432'),
    },
    'db_us': {
        'ENGINE'    : config("DB2_CONNECTION", default='django.db.backends.postgresql_psycopg2'),
        'USER'      : config('DB2_USER', default='root'),
        'NAME'      : config('DB2_NAME'),
        'PASSWORD'  : config('DB2_PASSWORD', default=''),
        'HOST'      : config('DB2_HOST', default='localhost'),
        'PORT'      : config('DB2_PORT', default='5432'),
    },

}

```

***  create data ke databa sesuai lokasi untuk menentukan database yang digunakan  ***

```
 def create(self, request, *args, **kwargs):
    # jika country == US maka database untuk    menyimapan menggunakan db_us
    if request.data['country'] == 'US':
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(using='db_us')
        return response.Response(serializer.data)
    return super().create(request, *args, **kwargs)

```

*** get all semua data dari 2 databae ***
```
# code

def list(self, request, *args, **kwargs):
    ``` list gabuangan dari dua database  ```
    data = list(chain(Warga.objects.using('db_us'), self.queryset))
    serialize = self.serializer_class(data, many=True)
    return response.Response(serialize.data)

[
	{
		"id": 1,
		"country": "US",
		"name": "RObin",
		"gender": "Fimale",
		"age": 2,
		"address": "Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186"
	},
	{
		"id": 2,
		"country": "US",
		"name": "Vincent",
		"gender": "Male",
		"age": 12,
		"address": "LA"
	},
	{
		"id": 21,
		"country": "US",
		"name": "MARSELO",
		"gender": "Male",
		"age": 23,
		"address": "LA city"
	},
	{
		"id": 23,
		"country": "US",
		"name": "ANTONIA",
		"gender": "Fimale",
		"age": 23,
		"address": "LA city"
	},
	{
		"id": 1,
		"country": "IN",
		"name": "M Hadi Sasmito",
		"gender": "Fimale",
		"age": 12,
		"address": "Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186"
	},
	{
		"id": 2,
		"country": "IN",
		"name": "M Hadi Sasmito",
		"gender": "Male",
		"age": 12,
		"address": "Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186"
	},
	{
		"id": 17,
		"country": "IN",
		"name": "Tomy",
		"gender": "Male",
		"age": 23,
		"address": "LA city"
	},
	{
		"id": 22,
		"country": "IN",
		"name": "Anton",
		"gender": "Fimale",
		"age": 23,
		"address": "LA city"
	},
	{
		"id": 25,
		"country": "IN",
		"name": "ANTONIA",
		"gender": "Fimale",
		"age": 23,
		"address": "LA city"
	}
]
```

*** Data untuk db_us ***

``` 
+----+---------+---------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
| id | country | name    | gender | age | address                                                                                                               |
+----+---------+---------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
|  1 | US      | RObin   | Fimale |   2 | Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186 |
|  2 | US      | Vincent | Male   |  12 | LA                                                                                                                    |
| 21 | US      | MARSELO | Male   |  23 | LA city                                                                                                               |
| 23 | US      | ANTONIA | Fimale |  23 | LA city                                                                                                               |
+----+---------+---------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
```

*** Data untuk db_id ***

``` 
+----+---------+----------------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
| id | country | name           | gender | age | address                                                                                                               |
+----+---------+----------------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
|  1 | IN      | M Hadi Sasmito | Fimale |  12 | Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186 |
|  2 | IN      | M Hadi Sasmito | Male   |  12 | Jl. Bantul km. 9, Juron, Rt/Rw : 19/00, Krandohan, Pendowoharjo, Kec. Sewon, Bantul, Daerah Istimewa Yogyakarta 55186 |
| 17 | IN      | Tomy           | Male   |  23 | LA city                                                                                                               |
| 22 | IN      | Anton          | Fimale |  23 | LA city                                                                                                               |
| 25 | IN      | ANTONIA        | Fimale |  23 | LA city                                                                                                               |
+----+---------+----------------+--------+-----+-----------------------------------------------------------------------------------------------------------------------+
5 rows in set (0.01 sec)
```