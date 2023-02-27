import 'package:dio/dio.dart';
import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key? key}) : super(key: key);

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  final dio = Dio();
  Response<dynamic>? res1;
  Response<dynamic>? res2;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("rich_menu_sample"),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: <Widget>[
            const Text(
              'API call test',
            ),
            ElevatedButton(
              child: const Text("Call API ①"),
              onPressed: () async {
                final response1 = await dio.get(
                    'https://b212sdavwi.execute-api.us-east-1.amazonaws.com/default/sample');
                print(response1);
                print("=================");
                print(response1.data);
                print("=================");
                print(response1.headers);
                print("=================");
                print(response1.requestOptions);
                print("=================");
                print(response1.statusCode);
                setState(() {
                  res1 = response1;
                });
              },
            ),
            Text("【↓response↓】\n $res1"),
            Container(
              margin: const EdgeInsets.only(top: 30),
            ),
            ElevatedButton(
              child: const Text("Call API ②"),
              onPressed: () async {
                final response2 = await dio.get(
                    'https://0jpvds5on1.execute-api.us-east-1.amazonaws.com/default/ricu_munu_sample');
                print(response2);
                print("=================");
                print(response2.data);
                print("=================");
                print(response2.headers);
                print("=================");
                print(response2.requestOptions);
                print("=================");
                print(response2.statusCode);
                setState(() {
                  res2 = response2;
                });
              },
            ),
            Text("【↓response↓】\n $res2"),
          ],
        ),
      ),
    );
  }
}
