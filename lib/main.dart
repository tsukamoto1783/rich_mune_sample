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
  final String apiGatewayEndpoint =
      "https://0jpvds5on1.execute-api.us-east-1.amazonaws.com/default/ricu_munu_sample";
  final dio = Dio();
  bool isVisible1 = false;
  bool isError1 = false;
  Response<dynamic>? res1;

  bool isVisible2 = false;
  bool isError2 = false;
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
                setState(() {
                  isVisible1 = false;
                  isVisible2 = false;
                });
                try {
                  final response1 =
                      await dio.get('$apiGatewayEndpoint?is_swithc=true');
                  res1 = response1;
                } catch (e) {
                  isError1 = true;
                  print(e);
                }

                setState(() {
                  isVisible1 = true;
                });
              },
            ),
            Visibility(
              visible: isVisible1,
              child: Column(
                children: [
                  const Text("【↓response↓】"),
                  Visibility(
                    visible: !isError1,
                    child: Text("$res1"),
                  ),
                  Visibility(
                    visible: isError1,
                    child: const Text("API呼び出しに失敗しました"),
                  ),
                ],
              ),
            ),
            Container(
              margin: const EdgeInsets.only(top: 30),
            ),
            ElevatedButton(
              child: const Text("Call API ②"),
              onPressed: () async {
                setState(() {
                  isVisible1 = false;
                  isVisible2 = false;
                });
                try {
                  final response1 =
                      await dio.get('$apiGatewayEndpoint?is_swithc=false');
                  res2 = response1;
                } catch (e) {
                  isError2 = true;
                  print(e);
                }

                setState(() {
                  isVisible2 = true;
                });
              },
            ),
            Visibility(
              visible: isVisible2,
              child: Column(
                children: [
                  const Text("【↓response↓】"),
                  Visibility(
                    visible: !isError2,
                    child: Text("$res2"),
                  ),
                  Visibility(
                    visible: isError2,
                    child: const Text("API呼び出しに失敗しました"),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }
}
