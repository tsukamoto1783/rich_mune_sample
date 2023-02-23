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
              'Api call test',
            ),
            ElevatedButton(
              child: const Text("Call API"),
              onPressed: () async {
                final response = await dio.get('https://httpbin.org/get');
                print(response);
                print("=================");
                print(response.data);
                print("=================");
                print(response.headers);
                print("=================");
                print(response.requestOptions);
                print("=================");
                print(response.statusCode);
              },
            )
          ],
        ),
      ),
    );
  }
}
