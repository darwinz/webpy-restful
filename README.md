# Web.py RESTful Thermostats API

#### Prerequisites


- Python2.7
- Web.py ([webpy.org](http://webpy.org/install))


#### Starting the Web Service

```bash
$ # define the port the service will run on
$ port="3000" ### or some other valid port
$ python main.py ${port}
```

#### GET list all thermostats

```bash
$ port="3000"
$ curl -XGET http://localhost:${port}/v1/thermostats | python -m json.tool
```

#### POST create a new thermostat

```bash
$ port="3000"
$ id="100"
$ curl -XPOST -d '{"Name": "New Thermostat", "Operating_Mode": "off", "Fan_Mode": "auto", "Cool_Set_Point": 68, "Heat_Set_Point": 63}' http://localhost:${port}/v1/thermostats | python -m json.tool
```

#### GET search for a single thermostat

```bash
$ port="3000"
$ id="100"
$ curl -XGET http://localhost:${port}/v1/thermostats/${id} | python -m json.tool
```

#### PUT update a single thermostat

```bash
$ port="3000"
$ id="100"
$ curl -XPUT -d '{"Name": "Updated Thermostat", "Operating_Mode": "off", "Fan_Mode": "auto", "Cool_Set_Point": 69, "Heat_Set_Point": 64}' http://localhost:${port}/v1/thermostats/${id} | python -m json.tool
```

#### DELETE a single thermostat

```bash
$ port="3000"
$ id="101"
$ curl -XDELETE http://localhost:${port}/v1/thermostats/${id} | python -m json.tool
```
